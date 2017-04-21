from social.models import SocialProfile
from activity.models import CustomerState
from loan_product.models import LoanProduct
from homepage_config import (
    ELIGIBILITY_TITLE, KYC_TITLE, LOAN_CONSTANTS, LOAN_PRODUCT_STATES, USER_STATES_PRE_LOAN_SPECIFICATION, USER_STATE_MESSAGES)


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
