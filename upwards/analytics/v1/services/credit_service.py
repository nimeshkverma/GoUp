import json
from decimal import Decimal
from analytics.models import Algo360, DeviceData, ScreenEventData, FieldEventData
from aadhaar.models import Aadhaar
from eligibility.models import Profession, Education, Finance
from loan_product.models import LoanProduct, BikeLoan
from customer.models import BankDetails
from social.models import SocialProfile
from pan.models import Pan
from common.v1.utils.general_utils import get_class, string_similarity
from django.conf import settings
from analytics_service_constants import (MAB_VARIABLES, SALARY_VARIABLE, CREDIT_REPORT_MAPPING,
                                         CREDIT_REPORT_VARIABLE_NAME_MAP, CREDIT_REPORT_SUBSECTION_ORDER,
                                         CREDIT_REPORT_SECTION_ORDER)


class CustomerCreditLimit(object):

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.limit = self.__get_limit()
        self.is_eligible = self.__is_eligible()

    def __get_minimum_average_balance(self, algo360_object):
        minimum_average_balance_list = []
        for minimum_average_balance_key in MAB_VARIABLES:
            if algo360_object.__dict__.get(minimum_average_balance_key, 0) != 'N.A':
                minimum_average_balance_list.append(
                    int(float(algo360_object.__dict__.get(minimum_average_balance_key, 0))))
        return min(minimum_average_balance_list) if minimum_average_balance_list else None

    def __get_algo360_salary(self, algo360_object):
        return algo360_object.__dict__.get(SALARY_VARIABLE) if algo360_object.__dict__.get(SALARY_VARIABLE) != 'N.A' else None

    def __get_limit_from_variables(self, salary, algo360_salary, minimum_average_balance):
        limit = 0
        if algo360_salary == None and minimum_average_balance == None:
            limit = salary / settings.CREDIT_ELIGIBILITY_FACTOR if salary else 0
        elif algo360_salary == None:
            if minimum_average_balance:
                limit = min(salary, minimum_average_balance) / \
                    settings.CREDIT_ELIGIBILITY_FACTOR if salary else minimum_average_balance / \
                    settings.CREDIT_ELIGIBILITY_FACTOR
            else:
                limit = salary / settings.CREDIT_ELIGIBILITY_FACTOR if salary else 0
        elif minimum_average_balance == None:
            if algo360_salary:
                limit = min(algo360_salary, salary) / \
                    settings.CREDIT_ELIGIBILITY_FACTOR if salary else algo360_salary / \
                    settings.CREDIT_ELIGIBILITY_FACTOR
            else:
                limit = salary / settings.CREDIT_ELIGIBILITY_FACTOR if salary else 0
        else:
            limit = min(min(algo360_salary, minimum_average_balance), salary) / \
                settings.CREDIT_ELIGIBILITY_FACTOR if salary else min(
                algo360_salary, minimum_average_balance) / settings.CREDIT_ELIGIBILITY_FACTOR
        return int(limit)

    def __get_limit(self):
        minimum_average_balance = None
        algo360_salary = None
        salary = None
        algo360_objects = Algo360.objects.filter(customer_id=self.customer_id)
        if algo360_objects:
            minimum_average_balance = self.__get_minimum_average_balance(algo360_objects[
                                                                         0])
            algo360_salary = self.__get_algo360_salary(algo360_objects[0])
        profession_objects = Profession.objects.filter(
            customer_id=self.customer_id)

        if profession_objects:
            salary = profession_objects[0].salary
        return self.__get_limit_from_variables(salary, algo360_salary, minimum_average_balance)

    def __is_eligible(self):
        is_eligible = False
        if self.limit >= settings.ELIGIBILITY_LIMIT['lower']:
            is_eligible = True
        return is_eligible


class CreditReport(object):

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.customer_credit_limit = CustomerCreditLimit(
            self.customer_id).limit
        self.data = self.__get_report_data()
        self.context_data = self.__get_context_data()

    def __get_model_data(self):
        data = dict()
        for model_key, model_data in CREDIT_REPORT_MAPPING.iteritems():
            data[model_key] = {field_key: {'display_name': field_value, 'value': None}
                               for field_key, field_value in CREDIT_REPORT_MAPPING[model_key]['fields'].iteritems()}
            model_class = get_class(model_data['model_class'])
            model_objects = model_class.objects.filter(
                customer_id=self.customer_id)
            if model_objects:
                model_object = model_objects[len(model_objects) - 1]
                for field in data[model_key].keys():
                    data[model_key][field]['value'] = reduce(
                        getattr, field.split('__'), model_object)
        return data

    def __get_device_data(self):
        data = {
            'Call & SMS Log Data': {
            },
        }
        device_data_objects = DeviceData.objects.filter(customer_id=self.customer_id).order_by(
            'data_type', 'attribute', 'weekday_type', 'day_hour_type')
        for device_data_object in device_data_objects:
            key = "{data_type}_{status}_{attribute}_{weekday_type}_{day_hour_type}".format(data_type=device_data_object.data_type,
                                                                                           status=device_data_object.status,
                                                                                           attribute=device_data_object.attribute,
                                                                                           weekday_type=device_data_object.weekday_type,
                                                                                           day_hour_type=device_data_object.day_hour_type)
            display_name = "Customer's {attribute} of {status} {data_type} in {weekday_type} in {day_hour_type} time".format(data_type=device_data_object.data_type,
                                                                                                                             status=device_data_object.status,
                                                                                                                             attribute=device_data_object.attribute,
                                                                                                                             weekday_type=device_data_object.weekday_type,
                                                                                                                             day_hour_type=device_data_object.day_hour_type)
            if device_data_object.attribute in ["Duration Ratio", "Count Ratio"]:
                display_name += " (%)"
            elif display_name in ["Duration"]:
                display_name += " (Seconds)"
            else:
                pass
            data['Call & SMS Log Data'][key] = {
                'display_name': display_name,
                'value': float(device_data_object.value),
            }
        return data

    def __screenevent_data(self):
        data = {
            'Screen Event Data': {
            },
        }
        screenevent_data_objects = ScreenEventData.objects.filter(
            customer_id=self.customer_id)
        for screenevent_data_object in screenevent_data_objects:
            key_prefix = "{screen}_{mode}".format(screen=screenevent_data_object.screen,
                                                  mode=screenevent_data_object.mode)
            session_display_name = "Customer's Number of Sessions at {screen} screen in {mode} mode".format(screen=screenevent_data_object.screen,
                                                                                                            mode=screenevent_data_object.mode)
            timespent_display_name = "Customer's Time spent at {screen} screen in {mode} mode".format(screen=screenevent_data_object.screen,
                                                                                                      mode=screenevent_data_object.mode)
            data['Screen Event Data'][key_prefix + "_session"] = {
                'display_name': session_display_name,
                'value': int(screenevent_data_object.sessions)
            }
            data['Screen Event Data'][key_prefix + "_timespent"] = {
                'display_name': timespent_display_name,
                'value': int(screenevent_data_object.time_spent)
            }
        return data

    def __fieldevent_data(self):
        data = {
            'Field Event Data': {
            },
        }
        fieldevent_data_objects = FieldEventData.objects.filter(
            customer_id=self.customer_id)
        for fieldevent_data_object in fieldevent_data_objects:
            key_prefix = "{screen}_{mode}_{field}".format(screen=fieldevent_data_object.screen,
                                                          mode=fieldevent_data_object.mode,
                                                          field=fieldevent_data_object.field)
            edits_display_name = "Customer's Number of Changes in {field} field at {screen} screen in {mode} mode".format(screen=fieldevent_data_object.screen,
                                                                                                                          mode=fieldevent_data_object.mode,
                                                                                                                          field=fieldevent_data_object.field)
            deviation_display_name = "Customer's Input Deviation in {field} field at {screen} screen in {mode} mode".format(screen=fieldevent_data_object.screen,
                                                                                                                            mode=fieldevent_data_object.mode,
                                                                                                                            field=fieldevent_data_object.field)
            data['Field Event Data'][key_prefix + "_edits"] = {
                'display_name': edits_display_name,
                'value': int(fieldevent_data_object.edits)
            }
            data['Field Event Data'][key_prefix + "_deviation"] = {
                'display_name': deviation_display_name,
                'value': int(fieldevent_data_object.deviation)
            }
        return data

    def __get_aadhaar_data(self):
        data = {
            'AADHAAR': {
                'ekyc_applicable': {
                    'display_name': 'EKYC Applicable',
                    'value': 'No',
                },
                'dob': {
                    'display_name': 'Date of Birth of the Customer in AADHAAR',
                    'value': None,
                },
            }
        }
        aadhaar_objects = Aadhaar.objects.filter(customer_id=self.customer_id)
        if aadhaar_objects:
            data['AADHAAR']['dob']['value'] = aadhaar_objects[
                len(aadhaar_objects) - 1].dob
            if aadhaar_objects[len(aadhaar_objects) - 1].first_name_source == 'ekyc':
                data['AADHAAR']['ekyc_applicable']['value'] = 'Yes'
        return data

    def __update_algo360_variables(self, report_data):
        algo360_objects = Algo360.objects.filter(customer_id=self.customer_id)
        if algo360_objects:
            for algo360_variable_data in json.loads(algo360_objects[len(algo360_objects) - 1].algo360_data):
                variable_key = algo360_variable_data.keys()[0] if algo360_variable_data and isinstance(
                    algo360_variable_data, dict) else None
                if variable_key in CREDIT_REPORT_VARIABLE_NAME_MAP['SMS Scraping']:
                    report_data['SMS Scraping'][variable_key] = {
                        'display_name': CREDIT_REPORT_VARIABLE_NAME_MAP['SMS Scraping'][variable_key],
                        'value': round(float(algo360_variable_data[variable_key]), 2)
                    }
        return report_data

    def __salary_deviation_percentage(self, base_salary, deviated_salary):
        if deviated_salary and base_salary:
            return round((int(deviated_salary) - int(base_salary)) * 100.0 / int(base_salary), 2)
        else:
            return 0

    def __salary_deviation(self, report_data):
        sms_salary = report_data['SMS Scraping']['salary']['value'] if report_data[
            'SMS Scraping']['salary']['value'] != 'N.A' else 0
        data = {
            'Salary Deviation': {
                'base_salary': {
                    'display_name': 'Type Of Salary Taken As Base Value',
                    'value': 'Salary Disclosed By Customer In Eligibility Section (Rs)'
                },
                'eligibility_salary': {
                    'display_name': 'Salary Value Disclosed By Customer In Eligibility Section (Rs)',
                    'value': report_data['Profession']['salary']['value']
                },
                'loan_specification_salary': {
                    'display_name': 'Salary Value Disclosed By Customer In Loan Specification Section (Rs)',
                    'value': report_data['Loan Product']['monthly_income']['value']
                },
                'sms_salary': {
                    'display_name': 'Salary Value Obtained By SMS (Rs)',
                    'value': sms_salary
                },
                'loan_specification_salary_deviation': {
                    'display_name': 'Loan Specification Section Salary deviation From Eligibility Section Salary (%)',
                    'value': self.__salary_deviation_percentage(report_data['Profession']['salary']['value'], report_data['Loan Product']['monthly_income']['value'])
                },
                'sms_salary_deviation': {
                    'display_name': 'SMS Salary Deviation From Eligibility Section Salary (%)',
                    'value': self.__salary_deviation_percentage(report_data['Profession']['salary']['value'], sms_salary)
                },

            }
        }
        return data

    def __dob_deviation(self, report_data):
        aadhaar_dob = report_data['AADHAAR']['dob']['value']
        pan_dob = report_data['PAN']['dob']['value'] if report_data['PAN'][
            'dob']['value'] else report_data['AADHAAR']['dob']['value']

        data = {
            'DOB Deviation': {
                'pan_dob': {
                    'display_name': 'Date Of Birth Of The Customer In PAN',
                    'value': pan_dob,
                },
                'aadhaar_dob': {
                    'display_name': 'Date Of Birth Of The Customer In AADHAAR',
                    'value': aadhaar_dob,
                },
                'aadhaar_pan_dob': {
                    'display_name': 'Is The Date Of Birth Of The Customer Same On The AADHAAR And PAN',
                    'value': 'Yes',
                },
            }
        }
        return data

    def __get_social_name(self):
        name = ''
        social_profile_objects = SocialProfile.objects.filter(
            customer_id=self.customer_id).order_by('-platform')
        if social_profile_objects:
            name = social_profile_objects[
                0].first_name + ' ' + social_profile_objects[0].last_name
        return name

    def __get_bank_holder_name(self):
        name = ''
        bank_detail_objects = BankDetails.objects.filter(
            customer_id=self.customer_id)
        if bank_detail_objects:
            name = bank_detail_objects[0].account_holder_name
        return name

    def __get_aadhaar_name(self):
        name = ''
        aadhaar_objects = Aadhaar.objects.filter(
            customer_id=self.customer_id)
        if aadhaar_objects:
            name = aadhaar_objects[0].first_name + \
                ' ' + aadhaar_objects[0].last_name
        return name

    def __name_deviation(self, report_data):
        social_name = self.__get_social_name()
        bank_holder_name = self.__get_bank_holder_name()
        aadhaar_name = self.__get_aadhaar_name()
        pan_name = aadhaar_name

        data = {
            'Name Deviation': {
                'social_name': {
                    'display_name': 'Customer Name From Social Media',
                    'value': social_name,
                },
                'bank_holder_name': {
                    'display_name': 'Customer Name From Bank Details',
                    'value': bank_holder_name,
                },
                'aadhaar_name': {
                    'display_name': 'Customer Name From Aadhaar',
                    'value': aadhaar_name,
                },
                'pan_name': {
                    'display_name': 'Customer Name From PAN ',
                    'value': pan_name,
                },
                'social_pan_name_deviation': {
                    'display_name': 'Deviation Between Customer Social Media And PAN Name (%)',
                    'value': 100 * (1 - string_similarity(social_name, pan_name))
                },
                'pan_aadhaar_name_deviation': {
                    'display_name': 'Deviation Between Customer PAN Name And Aadhaar (%)',
                    'value': 100 * (1 - string_similarity(pan_name, aadhaar_name))
                },
                'aadhaar_bank_name_deviation': {
                    'display_name': 'Deviation Between Aadhaar And Bank Holder Name (%)',
                    'value': 100 * (1 - string_similarity(aadhaar_name, bank_holder_name))
                },
                'bank_social_name_deviation': {
                    'display_name': 'Deviation Between Customers Bank Holder And Social Media Name (%)',
                    'value': 100 * (1 - string_similarity(bank_holder_name, social_name))
                },

            }
        }
        return data

    def __dummy_processing(self, report_data):
        report_data['PAN']['status']['value'] = 'Verified'
        report_data['PAN']['cibil_score'] = {
            'display_name': 'CIBIL Score Of The Customer',
            'value': 'Not found',
        }
        report_data['PAN']['cibil_existing_emi'] = {
            'display_name': 'Is There A CIBIL Score Vs. Existing EMI Mismatch For The customer?',
            'value': 'No',
        }
        report_data['SMS Scraping']['online_salary_payment_mode_verified'] = {
            'display_name': 'Online Salary Payment Mode Is Verified?',
            'value': 'No'
        }
        report_data['Profession']['upwards_prefered_partner'] = {
            'display_name': 'Upwards Preferred Partner Company',
            'value': 'Yes'
        }
        report_data['PAN']['dob']['value'] = report_data[
            'AADHAAR']['dob']['value']
        return report_data

    def __get_report_data(self):
        report_data = self.__get_model_data()
        report_data.update(self.__get_aadhaar_data())
        report_data.update(self.__get_device_data())
        report_data.update(self.__name_deviation(report_data))
        report_data.update(self.__salary_deviation(report_data))
        report_data.update(self.__dob_deviation(report_data))
        report_data.update(self.__screenevent_data())
        report_data.update(self.__fieldevent_data())

        report_data = self.__update_algo360_variables(report_data)
        report_data = self.__dummy_processing(report_data)
        return report_data

    def __process_context_value(self, value):
        if type(value) in [Decimal, float]:
            return round(value, 2)
        if type(value) == bool:
            return 'Yes' if value else 'No'
        return str(value) if value else 'N.A'

    def __get_context_data(self):
        context_data = []
        for section in CREDIT_REPORT_SECTION_ORDER:
            section_data = []
            for subsection in CREDIT_REPORT_SUBSECTION_ORDER[section]:
                if self.data[section].get(subsection):
                    section_data.append({
                        'display_name': self.data[section][subsection]['display_name'],
                        'value': self.__process_context_value(self.data[section][subsection]['value']),
                    })
            context_data.append({
                'name': section,
                'data': section_data
            })
        return {'data': context_data}
