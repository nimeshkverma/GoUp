from django.conf import settings
from activity.model_constants import (UNKNOWN_STATE,
                                      SIGN_UP_STATE,
                                      LOAN_PRODUCT_SUBMIT_STATE,
                                      PAN_SUBMIT_STATE,
                                      PROFESSIONAL_SUBMIT_STATE,
                                      FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE,
                                      EDUCATION_SUBMIT_STATE,
                                      FINANCE_SUBMIT_EMAIL_VERIFIED_STATE,
                                      ELIGIBILITY_SUBMIT_STATE,
                                      AADHAAR_SUBMIT_STATE,
                                      AADHAAR_DETAIL_SUBMIT_STATE,
                                      BANK_DETAIL_SUBMIT_STATE,
                                      PERSONAL_CONTACT_SUBMIT_STATE,
                                      DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE,
                                      DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE,
                                      KYC_SUBMIT_STATE,
                                      ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE,
                                      ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE,
                                      ELIGIBILITY_APPROVED_KYC_REJECTED_STATE,
                                      ELIGIBILITY_APPROVED_KYC_APPROVED_STATE,
                                      LOAN_SPECIFICATION_REVIEWED_STATE,
                                      LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE,
                                      AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE,
                                      LOAN_APPLICATION_PROCCESSED_STATE,
                                      LOAN_APPLICATION_ERRORED_STATE,)

ELIGIBILITY_TITLE = "Eligibility Check"
KYC_TITLE = "KYC & Document Upload"

LOAN_CONSTANTS = {
    'loan_amount_maximum': 100000,
    'loan_amount_minimum': 10000,
    'loan_tenure_maximum': 24,
    'loan_tenure_minimum': 3,
    'loan_increment_value': 20000,
    'number_of_increments': 5,
    'rate_of_interest': settings.LOAN_INTEREST_RATE,
    'loan_tenure': {
        '0-10000': {
            'maximum_tenure': 6,
            'minimum_tenure': 3
        },
        '10000-20000': {
            'maximum_tenure': 6,
            'minimum_tenure': 3
        },
        '20000-30000': {
            'maximum_tenure': 6,
            'minimum_tenure': 3
        },
        '30000-40000': {
            'maximum_tenure': 6,
            'minimum_tenure': 3
        },
        '50000-100000': {
            'maximum_tenure': 24,
            'minimum_tenure': 3,
        },
    }
}

LOAN_PRODUCT_STATES = [
    UNKNOWN_STATE,
    SIGN_UP_STATE,
]

USER_STATES_PRE_LOAN_SPECIFICATION = [
    LOAN_PRODUCT_SUBMIT_STATE,
    PAN_SUBMIT_STATE,
    PROFESSIONAL_SUBMIT_STATE,
    FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE,
    EDUCATION_SUBMIT_STATE,
    FINANCE_SUBMIT_EMAIL_VERIFIED_STATE,
    ELIGIBILITY_SUBMIT_STATE,
    AADHAAR_SUBMIT_STATE,
    AADHAAR_DETAIL_SUBMIT_STATE,
    BANK_DETAIL_SUBMIT_STATE,
    PERSONAL_CONTACT_SUBMIT_STATE,
    DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE,
    DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE,
    KYC_SUBMIT_STATE,
    ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE,
    ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE,
    ELIGIBILITY_APPROVED_KYC_REJECTED_STATE,
    ELIGIBILITY_APPROVED_KYC_APPROVED_STATE,
]

USER_STATES_POST_LOAN_SPECIFICATION_PRE_LOAN_AMOUNT_TRANSFERED = [
    LOAN_SPECIFICATION_REVIEWED_STATE,
    LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE,
    AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE,
    LOAN_APPLICATION_PROCCESSED_STATE,
    LOAN_APPLICATION_ERRORED_STATE,

]

USER_STATE_MESSAGES = {
    UNKNOWN_STATE: {
        'eligibility': {
            'message': 'Please start your application by completing this section',
            'completion_percentage': 0,
        },
        'kyc': {
            'message': 'Please start your application by completing this section',
            'completion_percentage': 0,
        },
    },
    SIGN_UP_STATE: {
        'eligibility': {
            'message': 'Please start your application by completing this section',
            'completion_percentage': 0,
        },
        'kyc': {
            'message': "Please complete the '" + ELIGIBILITY_TITLE + "' section prior to this section",
            'completion_percentage': 0,
        },
    },
    LOAN_PRODUCT_SUBMIT_STATE: {
        'eligibility': {
            'message': 'Please provide your Eligibility Information.',
            'completion_percentage': 0,
        },
        'kyc': {
            'message': "Please complete the '" + ELIGIBILITY_TITLE + "' section prior to this section",
            'completion_percentage': 0,
        },
    },
    PAN_SUBMIT_STATE: {
        'eligibility': {
            'message': 'Please provide your employment details to continue',
            'completion_percentage': 20,
        },
        'kyc': {
            'message': "Please complete the '" + ELIGIBILITY_TITLE + "' section prior to this section",
            'completion_percentage': 0,
        },
    },
    PROFESSIONAL_SUBMIT_STATE: {
        'eligibility': {
            'message': 'Please provide your educational details to continue',
            'completion_percentage': 50,
        },
        'kyc': {
            'message': "Please complete the '" + ELIGIBILITY_TITLE + "' section prior to this section",
            'completion_percentage': 0,
        },
    },
    EDUCATION_SUBMIT_STATE: {
        'eligibility': {
            'message': 'Please complete the last section to finish your eligibility check',
            'completion_percentage': 70,
        },
        'kyc': {
            'message': "Please complete the '" + ELIGIBILITY_TITLE + "' section prior to this section",
            'completion_percentage': 0,
        },
    },
    FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE: {
        'eligibility': {
            'message': "Please verify your 'Company Email' to continue",
            'completion_percentage': 90,
        },
        'kyc': {
            'message': "Please complete the '" + ELIGIBILITY_TITLE + "' section prior to this section",
            'completion_percentage': 0,
        },
    },
    FINANCE_SUBMIT_EMAIL_VERIFIED_STATE: {
        'eligibility': {
            'message': 'Please do a final review of the information to proceed',
            'completion_percentage': 95,
        },
        'kyc': {
            'message': "Please complete the '" + ELIGIBILITY_TITLE + "' section prior to this section",
            'completion_percentage': 0,
        },
    },
    ELIGIBILITY_SUBMIT_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed, Please proceed to '" + KYC_TITLE + "' section",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'Please complete your application by filling this section',
            'completion_percentage': 0,
        },
    },
    AADHAAR_SUBMIT_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed, Please complete the '" + KYC_TITLE + "' section",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'Please provide your KYC details to continue',
            'completion_percentage': 20,
        },
    },
    AADHAAR_DETAIL_SUBMIT_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed, Please complete the '" + KYC_TITLE + "' section",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'Please provide your banking details to continue',
            'completion_percentage': 40,
        },
    },
    BANK_DETAIL_SUBMIT_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed, Please complete the '" + KYC_TITLE + "' section",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'Please provide your personal contact details to continue',
            'completion_percentage': 60,
        },
    },
    PERSONAL_CONTACT_SUBMIT_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed, Please complete the '" + KYC_TITLE + "' section",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'We need some basic documents to finalize your application. Please upload to continue',
            'completion_percentage': 70,
        },
    },
    DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed, Please complete the '" + KYC_TITLE + "' section",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'Please verify your personal email to continue',
            'completion_percentage': 90,
        },
    },
    DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed, Please complete the '" + KYC_TITLE + "' section",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'Please do a final review of the information to proceed',
            'completion_percentage': 95,
        },
    },
    KYC_SUBMIT_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'All done! Please wait while we verify all details and get back.',
            'completion_percentage': 100,
        },
    },
    ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE: {
        'eligibility': {
            'message': 'Unfortunately, you are not eligible. Please reapply after sometime or contact us.',
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'Unfortunately, you are not eligible. Please reapply after sometime or contact us.',
            'completion_percentage': 100,
        },
    },
    ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'All done! Please wait while we verify all details and get back.',
            'completion_percentage': 100,
        },
    },
    ELIGIBILITY_APPROVED_KYC_REJECTED_STATE: {
        'eligibility': {
            'message': 'Unfortunately, we were not able to verify your KYC details. Please reapply later or contact us.',
            'completion_percentage': 100,
        },
        'kyc': {
            'message': 'Unfortunately, we were not able to verify your KYC details. Please reapply later or contact us.',
            'completion_percentage': 100,
        },
    },
    ELIGIBILITY_APPROVED_KYC_APPROVED_STATE: {
        'eligibility': {
            'message': "'" + ELIGIBILITY_TITLE + "' section Completed",
            'completion_percentage': 100,
        },
        'kyc': {
            'message': "Bingo, Your KYC verification is done! Please press the 'Proceed' button at the bottom of the screen.",
            'completion_percentage': 100,
        },
    },
    LOAN_SPECIFICATION_REVIEWED_STATE: {
        'message': "Please Procceed for Esigning the Loan Agreement.",
    },
    LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE: {
        'message': 'Please take a printout of the Loan Agreement emailed to you, Sign it at the specified loactions and send it us.'
    },
    AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE: {
        'message': 'Please wait while we disburse your loan amount'
    },
    LOAN_APPLICATION_PROCCESSED_STATE: {
        'message': 'Your loan amount has been disbursed and will reflect in your account in sometime'
    },
    LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE: {
        'message': 'Some error occured while disbursing your loan'
    },
}
