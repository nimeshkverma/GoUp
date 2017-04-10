from social.models import SocialProfile
from activity.models import CustomerState
# from participant.models import Borrower
from homepage_config import (ELIGIBILITY_TITLE, KYC_TITLE,
                             USER_STATES_WITH_ELIGIBILITY_AMOUNT, USER_STATE_MESSAGES, BORROWER_STATES)


class Homepage(object):

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.present_state = CustomerState.get_customer_present_state(
            self.customer_id)
        self.eligibility_amount = None
        self.data = self.__borrower_homepage_data(
        ) if self.present_state in BORROWER_STATES else self.__pre_borrower_homepage_data()

    def __get_mast_message(self, customer_profile):
        return "Hello {first_name} {last_name}!".format(first_name=customer_profile.get('first_name', 'User'), last_name=customer_profile.get('last_name', ''))

    def __get_eligibility_amount(self):
        eligibility_amount = None
        # if self.present_state in USER_STATES_WITH_ELIGIBILITY_AMOUNT:
        #     borrower_objects = Borrower.objects.filter(
        #         customer_id=self.customer_id)
        #     if borrower_objects:
        #         eligibility_amount = borrower_objects[0].credit_limit
        return eligibility_amount

    def __get_eligibility_section(self):
        self.eligibility_amount = self.__get_eligibility_amount()
        message = USER_STATE_MESSAGES.get(self.present_state, {}).get(
            'eligibility', {}).get('message', '')
        if self.eligibility_amount and '{amount}' in message:
            message = message.format(amount=self.eligibility_amount)
        section = {
            'title': ELIGIBILITY_TITLE,
            'completion_percentage': USER_STATE_MESSAGES.get(self.present_state, {}).get('eligibility', {}).get('completion_percentage', 0),
            'message': message,
        }
        return section

    def __get_kyc_section(self):
        section = {
            'title': KYC_TITLE,
            'completion_percentage': USER_STATE_MESSAGES.get(self.present_state, {}).get('kyc', {}).get('completion_percentage', 0),
            'message': USER_STATE_MESSAGES.get(self.present_state, {}).get('kyc', {}).get('message', ''),
        }
        return section

    def __pre_borrower_homepage_data(self):
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

    def __borrower_credit_data(self):
        borrower_credit_data = {
            'credit_limit': 'N/A',
            'credit_available': 'N/A',
            'is_eligible_for_loan': 'N/A'
        }
        # borrower_objects = Borrower.objects.filter(
        #     customer_id=self.customer_id)
        # if borrower_objects:
        #     borrower_credit_data[
        #         'credit_limit'] = borrower_objects[0].credit_limit
        #     credit_available = borrower_objects[
        #         0].credit_limit - borrower_objects[0].total_current_debt
        #     borrower_credit_data[
        #         'credit_available'] = credit_available if credit_available > 0 else 0
        #     borrower_credit_data['is_eligible_for_loan'] = borrower_objects[
        #         0].eligible_for_loan
        return borrower_credit_data

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

    def __borrower_homepage_data(self):
        homepage_data = {
            'customer': {
                'id': self.customer_id,
                'state': self.present_state,
                'customer_profile': self.__customer_profile(),
                'credit_limit': None,
                'credit_available': None,
                'is_eligible_for_loan': None,
            },
            'mast_message': "",
            'sections': {
                'eligibility': self.__get_eligibility_section(),
                'kyc': self.__get_kyc_section(),
            },
        }
        homepage_data['customer'].update(self.__borrower_credit_data())
        return homepage_data
