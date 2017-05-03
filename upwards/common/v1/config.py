from django.conf import settings
from activity.model_constants import CUSTOMER_STATE_ORDER_LIST
from eligibility.models import MARITAL_STATUS_CHOICES, VEHICLE_TYPE_CHOICES, NATURE_OF_WORK_CHOICES
from aadhaar.models import AADHAAR_DATA_SOURCE_CHOICES
from documents.models import DOCUMENT_STATUS_CHOICES
from messenger.models import MESSAGE_TYPE_CHOICES
from social.models import PLATFORM_CHOICES, SOURCE_CHOICES
from analytics.models import LOG_TYPE_CHOICES
from common.models import OrganisationType, SalaryPaymentMode, ProfessionType, College, Company, Bike, LoanPurpose, GENDER_CHOICES
from . serializers import SalaryPaymentModeSerializer, OrganisationTypeSerializer, ProfessionTypeSerializer, CompanySerializer, CollegeSerializer, BikeSerializer, LoanPurposeSerializer
from customer.v1.service.homepage_config import LOAN_CONSTANTS


class Config(object):

    def __init__(self):
        self.data = self.__get_data()

    def __get_base_url(self):
        return settings.BASE_URL

    def __get_versions(self):
        return settings.VERSIONS

    def __get_versioned_base_url(self):
        return settings.VERSIONED_BASE_URL

    def __get_post_otp_message(self):
        return settings.POST_OTP_MESSAGE

    def __get_customer_default_profile_pic(self):
        return settings.CUSTOMER_DEFAULT_PROFILE_PIC

    def __get_data(self):
        config_data = {
            'user_state': CUSTOMER_STATE_ORDER_LIST,
            'base_url': self.__get_base_url(),
            'versions': self.__get_versions(),
            'versioned_base_url': self.__get_versioned_base_url(),
            'post_otp_message': self.__get_post_otp_message(),
            'customer_default_profile_pic': self.__get_customer_default_profile_pic(),
            'loan_constants': LOAN_CONSTANTS,
        }
        return config_data


class DropdownData(object):

    def list_tuple_to_list(self, tuple_list, index):
        output_list = []
        for tuple_data in tuple_list:
            output_list.append(str(tuple_data[0]).title())
        return output_list

    def __init__(self):
        self.data = self.__get_data()

    def __get_profession_type(self):
        profession_type_objects = ProfessionType.objects.all()
        return ProfessionTypeSerializer(profession_type_objects, many=True).data

    def __get_salary_payment_mode(self):
        salary_payment_mode_objects = SalaryPaymentMode.objects.all()
        return SalaryPaymentModeSerializer(salary_payment_mode_objects, many=True).data

    def __get_organisation_type(self):
        organisation_type_objects = OrganisationType.objects.all()
        return OrganisationTypeSerializer(organisation_type_objects, many=True).data

    def __get_company_list(self):
        company_objects = Company.objects.all()
        return CompanySerializer(company_objects, many=True).data

    def __get_college_list(self):
        college_objects = College.objects.all()
        return CollegeSerializer(college_objects, many=True).data

    def __get_bike_list(self):
        bike_objects = Bike.objects.all()
        return BikeSerializer(bike_objects, many=True).data

    def __get_loan_purpose_list(self):
        loan_purpose_objects = LoanPurpose.objects.all()
        return LoanPurposeSerializer(loan_purpose_objects, many=True).data

    def __get_data(self):
        dropdown_data = {
            'salary_payment_mode': self.__get_salary_payment_mode(),
            'organisation_type': self.__get_organisation_type(),
            'profession_type': self.__get_profession_type(),
            'company': self.__get_company_list(),
            'college': self.__get_college_list(),
            'bike': self.__get_bike_list(),
            'loan_purpose': self.__get_loan_purpose_list(),
            'maritial_status': self.list_tuple_to_list(MARITAL_STATUS_CHOICES, 0),
            'vehicle_type': self.list_tuple_to_list(VEHICLE_TYPE_CHOICES, 0),
            'nature_of_work': self.list_tuple_to_list(NATURE_OF_WORK_CHOICES, 0),
            'aadhaar_data_source': self.list_tuple_to_list(AADHAAR_DATA_SOURCE_CHOICES, 0),
            'gender': self.list_tuple_to_list(GENDER_CHOICES, 0),
            'document_status': self.list_tuple_to_list(DOCUMENT_STATUS_CHOICES, 0),
            'email_type': self.list_tuple_to_list(MESSAGE_TYPE_CHOICES, 0),
            'social_login_source': self.list_tuple_to_list(SOURCE_CHOICES, 0),
            'social_login_platform': self.list_tuple_to_list(PLATFORM_CHOICES, 0),
            'log_type': self.list_tuple_to_list(LOG_TYPE_CHOICES, 0),
        }
        return dropdown_data
