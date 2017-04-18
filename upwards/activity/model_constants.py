from copy import deepcopy

UPWARDS = 'upwards'
CUSTOMER = 'customer'
NBFC = 'nbfc'
ACTOR_CHOICES = (
    (UPWARDS, 'upwards'),
    (CUSTOMER, 'customer'),
    (NBFC, 'nbfc'),
)


SIGN_UP = 'sign_up'
LOAN_PRODUCT_SUBMIT = 'loan_product_submit'
PAN_SUBMIT = 'pan_submit'
PROFESSIONAL_SUBMIT = 'professional_submit'
FINANCE_SUBMIT_EMAIL_UNVERIFIED = 'finance_submit_email_unverified'
EDUCATION_SUBMIT = 'education_submit'
FINANCE_SUBMIT_EMAIL_VERIFIED = 'finance_submit_email_verified'
ELIGIBILITY_SUBMIT = 'eligibility_submit'
AADHAAR_SUBMIT = 'aadhaar_submit'
AADHAAR_DETAIL_SUBMIT = 'aadhaar_detail_submit'
BANK_DETAIL_SUBMIT = 'bank_detail_submit'
PERSONAL_CONTACT_SUBMIT = 'personal_contact_submit'
DOCUMENT_SUBMIT_EMAIL_UNVERIFIED = 'document_submit_email_unverified'
DOCUMENT_SUBMIT_EMAIL_VERIFIED = 'document_submit_email_verified'
KYC_SUBMIT = 'kyc_submit'
ELIGIBILITY_REJECTED_KYC_SUBMIT = 'eligibility_rejected_kyc_submit'
ELIGIBILITY_APPROVED_KYC_PROCCESSING = 'eligibility_approved_kyc_proccessing'
ELIGIBILITY_APPROVED_KYC_REJECTED = 'eligibility_approved_kyc_rejected'
ELIGIBILITY_APPROVED_KYC_APPROVED = 'eligibility_approved_kyc_approved'
LOAN_SPECIFICATION_REVIEWED = 'loan_specification_reviewed'
LOAN_SUBMIT_AGGREMENT_UNSIGNED = 'loan_submit_aggrement_unsigned'
AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING = 'aggrement_signed_loan_application_proccessing'
LOAN_APPLICATION_PROCCESSED = 'loan_application_proccessed'
LOAN_APPLICATION_ERRORED = 'loan_application_errored'


CUSTOMER_ACTIVITY_TYPE_CHOICES = (
    (SIGN_UP, 'sign_up'),
    (LOAN_PRODUCT_SUBMIT, 'loan_product_submit'),
    (PAN_SUBMIT, 'pan_submit'),
    (PROFESSIONAL_SUBMIT, 'professional_submit'),
    (FINANCE_SUBMIT_EMAIL_UNVERIFIED, 'finance_submit_email_unverified'),
    (EDUCATION_SUBMIT, 'education_submit'),
    (FINANCE_SUBMIT_EMAIL_VERIFIED, 'finance_submit_email_verified'),
    (ELIGIBILITY_SUBMIT, 'eligibility_submit'),
    (AADHAAR_SUBMIT, 'aadhaar_submit'),
    (AADHAAR_DETAIL_SUBMIT, 'aadhaar_detail_submit'),
    (BANK_DETAIL_SUBMIT, 'bank_detail_submit'),
    (PERSONAL_CONTACT_SUBMIT, 'personal_contact_submit'),
    (DOCUMENT_SUBMIT_EMAIL_UNVERIFIED, 'document_submit_email_unverified'),
    (DOCUMENT_SUBMIT_EMAIL_VERIFIED, 'document_submit_email_verified'),
    (KYC_SUBMIT, 'kyc_submit'),
    (ELIGIBILITY_REJECTED_KYC_SUBMIT, 'eligibility_rejected_kyc_submit'),
    (ELIGIBILITY_APPROVED_KYC_PROCCESSING, 'eligibility_approved_kyc_proccessing'),
    (LOAN_SPECIFICATION_REVIEWED, 'loan_specification_reviewed'),
    (AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING,
     'aggrement_signed_loan_application_proccessing'),
    (LOAN_SUBMIT_AGGREMENT_UNSIGNED, 'loan_submit_aggrement_unsigned'),
)

UPWARDS_TYPE_CHOICES = (
    (ELIGIBILITY_APPROVED_KYC_REJECTED, 'eligibility_approved_kyc_rejected'),
    (ELIGIBILITY_APPROVED_KYC_APPROVED, 'eligibility_approved_kyc_approved'),
    (LOAN_APPLICATION_PROCCESSED, 'loan_application_proccessed'),
    (LOAN_APPLICATION_ERRORED, 'loan_application_errored'),
)

ACTIVITY_TYPE_CHOICES = CUSTOMER_ACTIVITY_TYPE_CHOICES and UPWARDS_TYPE_CHOICES

UNKNOWN_STATE = 'unknown'
SIGN_UP_STATE = 'sign_up'
LOAN_PRODUCT_SUBMIT_STATE = 'loan_product_submit'
PAN_SUBMIT_STATE = 'pan_submit'
PROFESSIONAL_SUBMIT_STATE = 'professional_submit'
FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE = 'finance_submit_email_unverified'
EDUCATION_SUBMIT_STATE = 'education_submit'
FINANCE_SUBMIT_EMAIL_VERIFIED_STATE = 'finance_submit_email_verified'
ELIGIBILITY_SUBMIT_STATE = 'eligibility_submit'
AADHAAR_SUBMIT_STATE = 'aadhaar_submit'
AADHAAR_DETAIL_SUBMIT_STATE = 'aadhaar_detail_submit'
BANK_DETAIL_SUBMIT_STATE = 'bank_detail_submit'
PERSONAL_CONTACT_SUBMIT_STATE = 'personal_contact_submit'
DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE = 'document_submit_email_unverified'
DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE = 'document_submit_email_verified'
KYC_SUBMIT_STATE = 'kyc_submit'
ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE = 'eligibility_rejected_kyc_submit'
ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE = 'eligibility_approved_kyc_proccessing'
ELIGIBILITY_APPROVED_KYC_REJECTED_STATE = 'eligibility_approved_kyc_rejected'
ELIGIBILITY_APPROVED_KYC_APPROVED_STATE = 'eligibility_approved_kyc_approved'
LOAN_SPECIFICATION_REVIEWED_STATE = 'loan_specification_reviewed'
LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE = 'loan_submit_aggrement_unsigned'
AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE = 'aggrement_signed_loan_application_proccessing'
LOAN_APPLICATION_PROCCESSED_STATE = 'loan_application_proccessed'
LOAN_APPLICATION_ERRORED_STATE = 'loan_application_errored'

CUSTOMER_STATE_CHOICES = (
    (UNKNOWN_STATE, 'unknown'),
    (SIGN_UP_STATE, 'sign_up'),
    (LOAN_PRODUCT_SUBMIT_STATE, 'loan_product_submit'),
    (PAN_SUBMIT_STATE, 'pan_submit'),
    (PROFESSIONAL_SUBMIT_STATE, 'professional_submit'),
    (FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE, 'finance_submit_email_unverified'),
    (EDUCATION_SUBMIT_STATE, 'education_submit'),
    (FINANCE_SUBMIT_EMAIL_VERIFIED_STATE, 'finance_submit_email_verified'),
    (ELIGIBILITY_SUBMIT_STATE, 'eligibility_submit'),
    (AADHAAR_SUBMIT_STATE, 'aadhaar_submit'),
    (AADHAAR_DETAIL_SUBMIT_STATE, 'aadhaar_detail_submit'),
    (BANK_DETAIL_SUBMIT_STATE, 'bank_detail_submit'),
    (PERSONAL_CONTACT_SUBMIT_STATE, 'personal_contact_submit'),
    (DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE, 'document_submit_email_unverified'),
    (DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE, 'document_submit_email_verified'),
    (KYC_SUBMIT_STATE, 'kyc_submit'),
    (ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE, 'eligibility_rejected_kyc_submit'),
    (ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE,
     'eligibility_approved_kyc_proccessing'),
    (ELIGIBILITY_APPROVED_KYC_REJECTED_STATE, 'eligibility_approved_kyc_rejected'),
    (ELIGIBILITY_APPROVED_KYC_APPROVED_STATE, 'eligibility_approved_kyc_approved'),
    (LOAN_SPECIFICATION_REVIEWED_STATE, 'loan_specification_reviewed'),
    (LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE, 'loan_submit_aggrement_unsigned'),
    (AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE,
     'aggrement_signed_loan_application_proccessing'),
    (LOAN_APPLICATION_PROCCESSED_STATE, 'loan_application_proccessed'),
    (LOAN_APPLICATION_ERRORED_STATE, 'loan_application_errored'),
)

CUSTOMER_STATE_TREE = {
    UNKNOWN_STATE: {
        'from': [UNKNOWN_STATE],
        'to': [SIGN_UP_STATE]
    },
    SIGN_UP_STATE: {
        'from': [UNKNOWN_STATE],
        'to': [LOAN_PRODUCT_SUBMIT_STATE]
    },
    LOAN_PRODUCT_SUBMIT_STATE: {
        'from': [SIGN_UP_STATE],
        'to': [PAN_SUBMIT_STATE]
    },
    PAN_SUBMIT_STATE: {
        'from': [LOAN_PRODUCT_SUBMIT_STATE],
        'to': [PROFESSIONAL_SUBMIT_STATE]
    },
    PROFESSIONAL_SUBMIT_STATE: {
        'from': [PAN_SUBMIT_STATE],
        'to': [EDUCATION_SUBMIT_STATE]
    },
    EDUCATION_SUBMIT_STATE: {
        'from': [PROFESSIONAL_SUBMIT_STATE],
        'to': [FINANCE_SUBMIT_EMAIL_VERIFIED_STATE, FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE]
    },
    FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE: {
        'from': [EDUCATION_SUBMIT_STATE],
        'to': [FINANCE_SUBMIT_EMAIL_VERIFIED_STATE]
    },
    FINANCE_SUBMIT_EMAIL_VERIFIED_STATE: {
        'from': [EDUCATION_SUBMIT_STATE, FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE],
        'to': [ELIGIBILITY_SUBMIT_STATE]
    },
    ELIGIBILITY_SUBMIT_STATE: {
        'from': [FINANCE_SUBMIT_EMAIL_VERIFIED_STATE],
        'to': [AADHAAR_SUBMIT_STATE]
    },
    AADHAAR_SUBMIT_STATE: {
        'from': [ELIGIBILITY_SUBMIT_STATE],
        'to': [AADHAAR_DETAIL_SUBMIT_STATE],
    },
    AADHAAR_DETAIL_SUBMIT_STATE: {
        'from': [AADHAAR_SUBMIT_STATE],
        'to': [BANK_DETAIL_SUBMIT_STATE]
    },
    BANK_DETAIL_SUBMIT_STATE: {
        'from': [AADHAAR_DETAIL_SUBMIT_STATE],
        'to': [PERSONAL_CONTACT_SUBMIT_STATE]
    },
    PERSONAL_CONTACT_SUBMIT_STATE: {
        'from': [BANK_DETAIL_SUBMIT_STATE],
        'to': [DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE, DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE]
    },
    DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE: {
        'from': [PERSONAL_CONTACT_SUBMIT_STATE],
        'to': [DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE]
    },
    DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE: {
        'from': [PERSONAL_CONTACT_SUBMIT_STATE, DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE],
        'to': [KYC_SUBMIT_STATE]
    },
    KYC_SUBMIT_STATE: {
        'from': [DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE],
        'to': [ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE, ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE]
    },
    ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE: {
        'from': [KYC_SUBMIT_STATE],
        'to': []
    },
    ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE: {
        'from': [KYC_SUBMIT_STATE],
        'to': [ELIGIBILITY_APPROVED_KYC_REJECTED_STATE, ELIGIBILITY_APPROVED_KYC_APPROVED_STATE]
    },
    ELIGIBILITY_APPROVED_KYC_REJECTED_STATE: {
        'from': [ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE],
        'to': []
    },
    ELIGIBILITY_APPROVED_KYC_APPROVED_STATE: {
        'from': [ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE],
        'to': [LOAN_SPECIFICATION_REVIEWED_STATE]
    },
    LOAN_SPECIFICATION_REVIEWED_STATE: {
        'from': [ELIGIBILITY_APPROVED_KYC_APPROVED_STATE],
        'to': [AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE, LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE]
    },
    AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE: {
        'from': [LOAN_SPECIFICATION_REVIEWED_STATE, LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE],
        'to': [LOAN_APPLICATION_PROCCESSED_STATE, LOAN_APPLICATION_ERRORED_STATE]
    },
    LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE: {
        'from': [LOAN_SPECIFICATION_REVIEWED_STATE],
        'to': [AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE]
    },
    LOAN_APPLICATION_PROCCESSED_STATE: {
        'from': [AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE],
        'to': []
    },
    LOAN_APPLICATION_ERRORED_STATE: {
        'from': [AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE],
        'to': []
    },
}


CUSTOMER_STATE_ORDER_LIST = [
    UNKNOWN_STATE,
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
    LOAN_APPLICATION_ERRORED_STATE,
]
