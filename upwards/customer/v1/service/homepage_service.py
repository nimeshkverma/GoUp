from social.models import SocialProfile
from activity.models import CustomerState
from loan_product.models import LoanProduct
from homepage_config import (
    ELIGIBILITY_TITLE, KYC_TITLE, LOAN_CONSTANTS, LOAN_PRODUCT_STATES, USER_STATES_PRE_LOAN_SPECIFICATION,
    USER_STATES_POST_LOAN_SPECIFICATION_PRE_LOAN_AMOUNT_TRANSFERED, USER_STATE_MESSAGES, LOAN_APPLICATION_PROCCESSED_STATE,)


class Homepage(object):

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.present_state = CustomerState.get_customer_present_state(
            self.customer_id)
        self.data = self.__get_data()

    def __get_data(self):
        default_homepage = self.__default_homepage_data()
        if self.present_state in LOAN_PRODUCT_STATES:
            return self.__get_loan_product_homepage_data()
        if self.present_state in USER_STATES_PRE_LOAN_SPECIFICATION:
            return self.__pre_loan_specification_homepage_data()
        if self.present_state in USER_STATES_POST_LOAN_SPECIFICATION_PRE_LOAN_AMOUNT_TRANSFERED:
            return self.__post_loan_specification_pre_loan_amount_transfered_homepage_data()
        if self.present_state in [LOAN_APPLICATION_PROCCESSED_STATE]:
            return self.__dummy_homepage_data()
        return default_homepage

    def __customer_profile(self):
        social_data = {
            'google': {
                'first_name': None,
                'last_name': None,
                'profile_pic_link': None
            },
            'facebook': {
                'first_name': None,
                'last_name': None,
                'profile_pic_link': None
            }
        }
        social_profile_objects = SocialProfile.objects.filter(
            customer_id=self.customer_id)
        for social_profile_object in social_profile_objects:
            if social_profile_object.platform in social_data.keys():
                social_data[social_profile_object.platform][
                    'first_name'] = social_profile_object.first_name
                social_data[social_profile_object.platform][
                    'last_name'] = social_profile_object.last_name
                social_data[social_profile_object.platform][
                    'profile_pic_link'] = social_profile_object.profile_pic_link
        customer_data = {
            'first_name': social_data['google']['first_name'] if social_data['google']['first_name'] else social_data['facebook']['first_name'],
            'last_name': social_data['google']['last_name'] if social_data['google']['last_name'] else social_data['facebook']['last_name'],
            'profile_pic_link': social_data['google']['profile_pic_link'] if social_data['google']['profile_pic_link'] else social_data['facebook']['profile_pic_link'],
        }
        return customer_data

    def __get_mast_message(self, customer_profile):
        return "Hello {first_name} {last_name}!".format(first_name=customer_profile.get('first_name', 'User'), last_name=customer_profile.get('last_name', ''))

    def __get_eligibility_section(self):
        message = USER_STATE_MESSAGES.get(self.present_state, {}).get(
            'eligibility', {}).get('message', '')
        completion_percentage = USER_STATE_MESSAGES.get(self.present_state, {}).get(
            'eligibility', {}).get('completion_percentage', 0)
        section = {
            'title': ELIGIBILITY_TITLE,
            'completion_percentage': completion_percentage,
            'message': message,
        }
        return section

    def __get_kyc_section(self):
        message = USER_STATE_MESSAGES.get(
            self.present_state, {}).get('kyc', {}).get('message', '')
        completion_percentage = USER_STATE_MESSAGES.get(
            self.present_state, {}).get('kyc', {}).get('completion_percentage', 0)
        section = {
            'title': KYC_TITLE,
            'completion_percentage': completion_percentage,
            'message': message,
        }
        return section

    def __get_message_section(self):
        return USER_STATE_MESSAGES.get(self.present_state, {})

    def __get_loan_product_homepage_data(self):
        customer_profile = self.__customer_profile()
        homepage_data = {
            'customer': {
                'id': self.customer_id,
                'state': self.present_state,
                'customer_profile': customer_profile,
            },
            'mast_message': self.__get_mast_message(customer_profile),
            'loan_constants': LOAN_CONSTANTS,
        }
        return homepage_data

    def __pre_loan_specification_homepage_data(self):
        customer_profile = self.__customer_profile()
        homepage_data = {
            'customer': {
                'id': self.customer_id,
                'state': self.present_state,
                'customer_profile': customer_profile,
            },
            'mast_message': self.__get_mast_message(customer_profile),
            'sections': {
                'eligibility': self.__get_eligibility_section(),
                'kyc': self.__get_kyc_section(),
            },
        }
        return homepage_data

    def __default_homepage_data(self):
        customer_profile = self.__customer_profile()
        homepage_data = {
            'customer': {
                'id': self.customer_id,
                'state': self.present_state,
                'customer_profile': customer_profile,
            },
            'mast_message': self.__get_mast_message(customer_profile),
            'sections': {
            },
        }
        return homepage_data

    def __post_loan_specification_pre_loan_amount_transfered_homepage_data(self):
        customer_profile = self.__customer_profile()
        homepage_data = {
            'customer': {
                'id': self.customer_id,
                'state': self.present_state,
                'customer_profile': customer_profile,
            },
            'mast_message': self.__get_mast_message(customer_profile),
            'sections': self.__get_message_section(),
        }
        return homepage_data

    def __dummy_homepage_data(self):
        customer_profile = self.__customer_profile()
        homepage_data = {
            'customer': {
                'id': self.customer_id,
                'state': self.present_state,
                'customer_profile': customer_profile,
            },
            'mast_message': self.__get_mast_message(customer_profile),
            "sections": {
                "loan_details": {
                    "loan_amount": 20000,
                    "loan_interest": 0.03,
                    "emi": 2345,
                    "processing_fee": 500,
                    "tenure": 10
                },
                "emi_schedule": [
                    {
                        "due_date": "2017-05-26",
                        "serial_no": 1,
                        "emi": 2345,
                        "principal_outstanding": 20000,
                        "principal_paid": 1745,
                        "interest_paid": 600,
                        "month": "May"
                    },
                    {
                        "due_date": "2017-06-26",
                        "serial_no": 2,
                        "emi": 2345,
                        "principal_outstanding": 18256,
                        "principal_paid": 1797,
                        "interest_paid": 548,
                        "month": "June"
                    },
                    {
                        "due_date": "2017-07-26",
                        "serial_no": 3,
                        "emi": 2345,
                        "principal_outstanding": 16459,
                        "principal_paid": 1851,
                        "interest_paid": 494,
                        "month": "July"
                    },
                    {
                        "due_date": "2017-08-26",
                        "serial_no": 4,
                        "emi": 2345,
                        "principal_outstanding": 14608,
                        "principal_paid": 1907,
                        "interest_paid": 439,
                        "month": "August"
                    },
                    {
                        "due_date": "2017-09-26",
                        "serial_no": 5,
                        "emi": 2345,
                        "principal_outstanding": 12702,
                        "principal_paid": 1964,
                        "interest_paid": 382,
                        "month": "September"
                    },
                    {
                        "due_date": "2017-10-26",
                        "serial_no": 6,
                        "emi": 2345,
                        "principal_outstanding": 10738,
                        "principal_paid": 2023,
                        "interest_paid": 323,
                        "month": "October"
                    },
                    {
                        "due_date": "2017-11-26",
                        "serial_no": 7,
                        "emi": 2345,
                        "principal_outstanding": 8716,
                        "principal_paid": 2084,
                        "interest_paid": 262,
                        "month": "November"
                    },
                    {
                        "due_date": "2017-12-26",
                        "serial_no": 8,
                        "emi": 2345,
                        "principal_outstanding": 6632,
                        "principal_paid": 2146,
                        "interest_paid": 199,
                        "month": "December"
                    },
                    {
                        "due_date": "2018-01-26",
                        "serial_no": 9,
                        "emi": 2345,
                        "principal_outstanding": 4487,
                        "principal_paid": 2211,
                        "interest_paid": 135,
                        "month": "January"
                    },
                    {
                        "due_date": "2018-02-26",
                        "serial_no": 10,
                        "emi": 2345,
                        "principal_outstanding": 2277,
                        "principal_paid": 2277,
                        "interest_paid": 69,
                        "month": "Febrary"
                    }
                ],
                "repayment_breakup": {}
            }
        }
        return homepage_data
