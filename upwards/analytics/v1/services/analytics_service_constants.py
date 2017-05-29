CREDENTIALS_FILE = 'analytics/v1/services/algo360_credentials.json'

MAB_VARIABLES = ['monthly_average_balance_lifetime', 'monthly_average_balance_12',
                 'monthly_average_balance_6', 'monthly_average_balance_3', 'monthly_average_balance_1']
SALARY_VARIABLE = 'salary'

ALGO360_UPWARDS_MAPPING = {
    'var201093': 'monthly_average_balance_lifetime',
    'var201094': 'monthly_average_balance_12',
    'var201095': 'monthly_average_balance_6',
    'var201096': 'monthly_average_balance_3',
    'var201097': 'monthly_average_balance_1',
    'var201204': 'number_of_cheque_bounce_1',
    'var201203': 'number_of_cheque_bounce_3',
    'var202003': 'is_credit_card_overlimited',
    'var202064': 'credit_card_last_payment_due',
    'var101003': 'salary',
}

CREDIT_REPORT_MAPPING = {
    'LoanProduct': {
        'fields': {
            'monthly_income': 'Monthly Income Specified on Loan Specification Screen',
            'existing_emi': 'Any Existing EMIs',
            'loan_purpose__name': 'Purpose of the Loan'
        },
        'model_class': 'loan_product.models.LoanProduct',
    },
    'BikeLoan': {
        'fields': {
            'brand': 'Brand of the Bike',
            'model': 'Model of the Bike',
            'manufacturing_year': 'Manufacturing year of the Bike',
            'approximate_price': 'Approximate price of the Bike',
            'down_payment': 'Down Payment of the Bike',
        },
        'model_class': 'loan_product.models.BikeLoan',
    },
    'PAN': {
        'fields': {
            'is_verified': 'Is PAN verified',
            'title': 'Title of the Customer in PAN',
            'first_name': 'First Name of the Customer in PAN',
            'middle_name': 'First Name of the Customer in PAN',
            'last_name': 'Last Name of the Customer in PAN',
            'dob': 'Date of Birth of the Customer in PAN',
            'status': 'PAN Status of the Customer',
            'pan_updates': 'PAN Updates of the Customer',
        },
        'model_class': 'pan.models.Pan',
    },
    'Profession': {
        'fields': {
            'company': 'Name of the Company, where Customer works',
            'organisation_type__name': 'Organisation type of the Company, where Customer works',
            'salary_payment_mode__name': 'Salary Payment mode of the Customer',
            'profession_type__type_name': 'Profession Type of the Customer',
            'email': 'Professional Email of the Customer',
            'is_email_verified': 'Is Professional Email of the Customer Verified?',
            'department': "Company's Department where Customer works",
            'designation': 'Designation of the Customer',
            'office_city': 'City where Customer works',
            'phone_no': 'Professional Contact number of the Customer',
            'is_phone_no_verified': 'Is Professional Contact number of the Customer Verified?',
            'salary': 'Monthly Salary of the Customer',
            'total_experience': 'Total work experience of the Customer in months',
            'nature_of_work': 'Nature of Work of the Customer',
        },
        'model_class': 'eligibility.models.Profession',
    },
    'Education': {
        'fields': {
            'college': 'Last College attended by Customer',
            'qualification': 'Highest qualification of the Customer',
            'completion_year': 'Highest qualification completion year of the Customer',
        },
        'model_class': 'eligibility.models.Education',
    },
    'Finance': {
        'fields': {
            'any_active_loans': 'Any active loans taken by the Customer',
            'any_owned_vehicles': 'Any vehicle owned by the Customer',
            'vehicle_type': 'Type of vehicle owned by the Customer',
            'marital_status': 'Maritial Status of the Customer',
            'dependents': 'Number of Dependents on Customer',
        },
        'model_class': 'eligibility.models.Finance',
    },
    'Algo360': {
        'fields':     {
            'monthly_average_balance_lifetime': 'Monthly average balance of the Customer in his lifetime',
            'monthly_average_balance_12': 'Monthly average balance of the Customer in in last 12 months',
            'monthly_average_balance_6': 'Monthly average balance of the Customer in last 6 months',
            'monthly_average_balance_3': 'Monthly average balance of the Customer in last 3 months',
            'monthly_average_balance_1': 'Monthly average balance of the Customer in last 1 months',
            'number_of_cheque_bounce_1': 'Number of cheque bounced in last month',
            'number_of_cheque_bounce_3': 'Number of cheque bounced in last 3 month',
            'salary': 'Salary deduced from SMS data',
        },
        'model_class': 'analytics.models.Algo360',
    },
}

CREDIT_REPORT_VARIABLE_NAME_MAP = {
    'Algo360': {
        'var206002': 'Flag - Missed Loan Payments/ EMIs',
        'var206003': 'Number Of Loan Accounts Lifetime',
        'var206004': 'Number Of Loan Accounts Last 12 Months',
        'var206005': 'Number Of Loan Accounts Last 6 Months',
        'var206006': 'Number Of Loan Accounts Last 3 Months',
        'var206007': 'Number Of Loan Accounts Last 1 Month',
        'var206008': 'Number Of Loan Accounts Last 3 Months By Number Of Loan Accounts Last 6 Months',
        'var206009': 'Avg. Monthly Loan Liability Lifetime',
        'var206010': 'Avg. Monthly Loan Liability Last 12 Months',
        'var206011': 'Avg. Monthly Loan Liability Last 6 Months',
        'var206012': 'Avg. Monthly Loan Liability Last 3 Months ',
        'var206013': 'Avg. Monthly Loan Liability Last 1 Month',
        'var206020': 'Number Of Loan Payments Missed Lifetime',
        'var206021': 'Number Of Loan Payments Missed Last 12 Months',
        'var206022': 'Number Of Loan Payments Missed Last 6 Months',
        'var206023': 'Number Of Loan Payments Missed Last 3 Months',
        'var206024': 'Number Of Loan Payments Missed Last 1 Month',
        'var206036': 'Sender Name in Loans',
        'var206037': 'Loan Account Number',
        'var101001': 'Lifetime Available (In Months) / Data Available For Duration',
        'var201001': 'Number Of CASA Accounts',
        'var201002': 'Number Of Unique Banks Having CASA Relationships With',
        'var201003': 'Flag - Cheque Returned',
        'var301001': 'Flag - Postpaid On Mobile',
        'var201005': 'Time Since Last Negative Event',
        'var101002': 'Flag - Salaried',
        'var201086': 'Avg. Daily Closing Balance Lifetime',
        'var201087': 'Avg. Daily Closing Balance Last 12 Months ',
        'var201088': 'Avg. Daily Closing Balance Last 6 Months',
        'var201089': 'Avg. Daily Closing Balance Last 3 Months',
        'var201090': 'Avg. Daily Closing Balance Last 1 Month',
        'var201093': 'Monthly Average Balance Lifetime',
        'var201094': 'Monthly Average Balance Last 12 Months ',
        'var201095': 'Monthly Average Balance Last 6 Months',
        'var201096': 'Monthly Average Balance Last 3 Months',
        'var201097': 'Monthly Average Balance Last 1 Month',
        'var201200': 'Number Of Cheques Returned Lifetime',
        'var201201': 'Number Of Cheques Returned Last 12 Months',
        'var201202': 'Number Of Cheques Returned Last 6 Months',
        'var201203': 'Number Of Cheques Returned Last 3 Months',
        'var201204': 'Number Of Cheques Returned Last 1 Month',
        'var301007': 'Avg. Monthly Recharge Amount Lifetime',
        'var301008': 'Avg. Monthly Recharge Amount Last 12 Months',
        'var301009': 'Avg. Monthly Recharge Amount Last 6 Months',
        'var301010': 'Avg. Monthly Recharge Amount Last 3 Months',
        'var301011': 'Avg. Monthly Recharge Amount Last 1 Month',
        'var301014': 'Avg. Monthly Postpaid Bill Amount Lifetime',
        'var301015': 'Avg. Monthly Postpaid Bill Amount Last 12 Months',
        'var301016': 'Avg. Monthly Postpaid Bill Amount Last 6 Months ',
        'var301017': 'Avg. Monthly Postpaid Bill Amount Last 3 Month',
        'var601001': 'Number Of Ecom Purchases Lifetime',
        'var601002': 'Number Of Ecom Purchases Last 12 Months ',
        'var601003': 'Number Of Ecom Purchases Last 6 Months ',
        'var601004': 'Number Of Ecom Purchases Last 3 Months ',
        'var601005': 'Number Of Ecom Purchases Last 1 Month ',
        'var601006': 'Number Of Ecom Purchases Last 7 Days',
        'var601007': 'Avg Monthly Ecom Purchase Amount Life Time',
        'var601008': 'Avg Monthly Ecom Purchase Amount Last 12 Month',
        'var601009': 'Avg Monthly Ecom Purchase Amount Last 6 Month',
        'var601010': 'Avg Monthly Ecom Purchase Amount Last 3 Month',
        'var601011': 'Avg Monthly Ecom Purchase Amount Last 1 Month',
        'var601012': 'Avg Monthly Ecom Purchase Amount Last 7 Days',
        'var207001': 'Total Wallet Top-Up Lifetime',
        'var207002': 'Total Wallet Top-Up Last 360 Days',
        'var207003': 'Total Wallet Top-Up Last 180 Days',
        'var207004': 'Total Wallet Top-Up Last 90 Days',
        'var207005': 'Total Wallet Top-Up Last 30 Days',
        'var207006': 'Number Of Mobile Wallets',
        'var207007': 'Number Of Wallet Top-Up Lifetime',
        'var207008': 'Number Of Wallet Top-Up Last 360 Days',
        'var207009': 'Number Of Wallet Top-Up Last 180 Days',
        'var207010': 'Number Of Wallet Top-Up Last 90 Days',
        'var207011': 'Number Of Wallet Top-Up Last 30 Days',
        'var207012': 'Number Of Total Credit Transactions',
        'var207013': 'Number Of Total Debit Transactions',
        'var207014': 'Number Of Money Transfers (Debit)',
        'var207015': 'Number Of Money Transfers (Credit)',
        'var207016': 'Amount Of Total Credit Transactions',
        'var207017': 'Amount Of Total Debit Transactions',
        'var207018': 'Amount Of Money Transfers (Debit)',
        'var207019': 'Amount Of Money Transfers (Credit)',
    },
    'DeviceData': {
        'data_type': 'data_type',
        'status': 'status',
        'attribute': 'attribute',
        'weekday_type': 'weekday_type',
        'day_hour_type': 'day_hour_type',
        'value': 'value',
    },
}

CREDIT_REPORT_SECTION_ORDER = [
    'LoanProduct',
    'BikeLoan',
    'PAN',
    'Profession',
    'Education',
    'Finance',
    'AADHAAR',
    'SalaryDeviation',
    'NameDeviation',
    'DOBDeviation',
    'Algo360',
    'DeviceData',
    'ScreenEventData',
    'FieldEventData'
]

CREDIT_REPORT_SUBSECTION_ORDER = {
    'LoanProduct': [
        'loan_purpose__name',
        'monthly_income',
        'existing_emi',
    ],
    'BikeLoan': [
        'model_class',
        'brand',
        'down_payment',
        'manufacturing_year',
        'approximate_price',
    ],
    'PAN': [
        'status',
        'pan_updates',
        'first_name',
        'last_name',
        'middle_name',
        'title',
        'dob',
        'cibil_score',
        'cibil_existing_emi',
        'is_verified',
    ],
    'Profession': [
        'nature_of_work',
        'company',
        'organisation_type__name',
        'office_city',
        'upwards_prefered_partner',
        'profession_type__type_name',
        'department',
        'designation',
        'total_experience',
        'salary',
        'salary_payment_mode__name',
        'phone_no',
        'email',
        'is_phone_no_verified',
        'is_email_verified',
    ],
    'Education': [
        'qualification',
        'college',
        'completion_year',
    ],
    'Finance': [
        'any_active_loans',
        'marital_status',
        'dependents',
        'any_owned_vehicles',
        'vehicle_type',
    ],
    'AADHAAR': [
        'ekyc_applicable',
        'dob'
    ],
    'SalaryDeviation': [
        'loan_specification_salary',
        'eligibility_salary',
        'sms_salary',
        'base_salary',
        'loan_specification_salary_deviation',
        'sms_salary_deviation',
    ],
    'NameDeviation': [
        'social_name',
        'pan_name',
        'aadhaar_name',
        'bank_holder_name',
        'social_pan_name_deviation',
        'pan_aadhaar_name_deviation',
        'aadhaar_bank_name_deviation',
        'bank_social_name_deviation',
    ],
    'DOBDeviation': [
        "aadhaar_pan_dob",
        "pan_dob",
        "aadhaar_dob",
    ],
    'Algo360': [
        'var206002',
        'var206003',
        'var206004',
        'var206005',
        'var206006',
        'var206007',
        'var206008',
        'var206009',
        'var206010',
        'var206011',
        'var206012',
        'var206013',
        'var206020',
        'var206021',
        'var206022',
        'var206023',
        'var206024',
        'var206036',
        'var206037',
        'var101001',
        'var201001',
        'var201002',
        'var201003',
        'var301001',
        'var201005',
        'var101002',
        'var201086',
        'var201087',
        'var201088',
        'var201089',
        'var201090',
        'var201093',
        'var201094',
        'var201095',
        'var201096',
        'var201097',
        'var201200',
        'var201201',
        'var201202',
        'var201203',
        'var201204',
        'var301007',
        'var301008',
        'var301009',
        'var301010',
        'var301011',
        'var301014',
        'var301015',
        'var301016',
        'var301017',
        'var601001',
        'var601002',
        'var601003',
        'var601004',
        'var601005',
        'var601006',
        'var601007',
        'var601008',
        'var601009',
        'var601010',
        'var601011',
        'var601012',
        'var207001',
        'var207002',
        'var207003',
        'var207004',
        'var207005',
        'var207006',
        'var207007',
        'var207008',
        'var207009',
        'var207010',
        'var207011',
        'var207012',
        'var207013',
        'var207014',
        'var207015',
        'var207016',
        'var207017',
        'var207018',
        'var207019'
    ],
    'DeviceData': [
        'Call_Incoming_Count_Week_All',
        'Call_Incoming_Count_Week_Evening',
        'Call_Incoming_Count_Week_Late Night',
        'Call_Incoming_Count_Week_Morning',
        'Call_Incoming_Count_Week_Office Hours',
        'Call_Incoming_Count_Weekday_All',
        'Call_Incoming_Count_Weekday_Evening',
        'Call_Incoming_Count_Weekday_Late Night',
        'Call_Incoming_Count_Weekday_Morning',
        'Call_Incoming_Count_Weekday_Office Hours',
        'Call_Incoming_Count_Weekend_All',
        'Call_Incoming_Count_Weekend_Evening',
        'Call_Incoming_Count_Weekend_Late Night',
        'Call_Incoming_Count_Weekend_Morning',
        'Call_Incoming_Count_Weekend_Office Hours',
        'Call_Incoming_Duration_Week_All',
        'Call_Incoming_Duration_Week_Evening',
        'Call_Incoming_Duration_Week_Late Night',
        'Call_Incoming_Duration_Week_Morning',
        'Call_Incoming_Duration_Week_Office Hours',
        'Call_Incoming_Duration_Weekday_All',
        'Call_Incoming_Duration_Weekday_Evening',
        'Call_Incoming_Duration_Weekday_Late Night',
        'Call_Incoming_Duration_Weekday_Morning',
        'Call_Incoming_Duration_Weekday_Office Hours',
        'Call_Incoming_Duration_Weekend_All',
        'Call_Incoming_Duration_Weekend_Evening',
        'Call_Incoming_Duration_Weekend_Late Night',
        'Call_Incoming_Duration_Weekend_Morning',
        'Call_Incoming_Duration_Weekend_Office Hours',
        'Call_Outgoing_Count_Week_All',
        'Call_Outgoing_Count_Week_Evening',
        'Call_Outgoing_Count_Week_Late Night',
        'Call_Outgoing_Count_Week_Morning',
        'Call_Outgoing_Count_Week_Office Hours',
        'Call_Outgoing_Count_Weekday_All',
        'Call_Outgoing_Count_Weekday_Evening',
        'Call_Outgoing_Count_Weekday_Late Night',
        'Call_Outgoing_Count_Weekday_Morning',
        'Call_Outgoing_Count_Weekday_Office Hours',
        'Call_Outgoing_Count_Weekend_All',
        'Call_Outgoing_Count_Weekend_Evening',
        'Call_Outgoing_Count_Weekend_Late Night',
        'Call_Outgoing_Count_Weekend_Morning',
        'Call_Outgoing_Count_Weekend_Office Hours',
        'Call_Outgoing_Duration_Week_All',
        'Call_Outgoing_Duration_Week_Evening',
        'Call_Outgoing_Duration_Week_Late Night',
        'Call_Outgoing_Duration_Week_Morning',
        'Call_Outgoing_Duration_Week_Office Hours',
        'Call_Outgoing_Duration_Weekday_All',
        'Call_Outgoing_Duration_Weekday_Evening',
        'Call_Outgoing_Duration_Weekday_Late Night',
        'Call_Outgoing_Duration_Weekday_Morning',
        'Call_Outgoing_Duration_Weekday_Office Hours',
        'Call_Outgoing_Duration_Weekend_All',
        'Call_Outgoing_Duration_Weekend_Evening',
        'Call_Outgoing_Duration_Weekend_Late Night',
        'Call_Outgoing_Duration_Weekend_Morning',
        'Call_Outgoing_Duration_Weekend_Office Hours',
        'Call_Outgoing/Incoming_Count Ratio_Week_All',
        'Call_Outgoing/Incoming_Count Ratio_Week_Evening',
        'Call_Outgoing/Incoming_Count Ratio_Week_Late Night',
        'Call_Outgoing/Incoming_Count Ratio_Week_Morning',
        'Call_Outgoing/Incoming_Count Ratio_Week_Office Hours',
        'Call_Outgoing/Incoming_Count Ratio_Weekday_All',
        'Call_Outgoing/Incoming_Count Ratio_Weekday_Evening',
        'Call_Outgoing/Incoming_Count Ratio_Weekday_Late Night',
        'Call_Outgoing/Incoming_Count Ratio_Weekday_Morning',
        'Call_Outgoing/Incoming_Count Ratio_Weekday_Office Hours',
        'Call_Outgoing/Incoming_Count Ratio_Weekend_All',
        'Call_Outgoing/Incoming_Count Ratio_Weekend_Evening',
        'Call_Outgoing/Incoming_Count Ratio_Weekend_Late Night',
        'Call_Outgoing/Incoming_Count Ratio_Weekend_Morning',
        'Call_Outgoing/Incoming_Count Ratio_Weekend_Office Hours',
        'Call_Outgoing/Incoming_Duration Ratio_Week_All',
        'Call_Outgoing/Incoming_Duration Ratio_Week_Evening',
        'Call_Outgoing/Incoming_Duration Ratio_Week_Late Night',
        'Call_Outgoing/Incoming_Duration Ratio_Week_Morning',
        'Call_Outgoing/Incoming_Duration Ratio_Week_Office Hours',
        'Call_Outgoing/Incoming_Duration Ratio_Weekday_All',
        'Call_Outgoing/Incoming_Duration Ratio_Weekday_Evening',
        'Call_Outgoing/Incoming_Duration Ratio_Weekday_Late Night',
        'Call_Outgoing/Incoming_Duration Ratio_Weekday_Morning',
        'Call_Outgoing/Incoming_Duration Ratio_Weekday_Office Hours',
        'Call_Outgoing/Incoming_Duration Ratio_Weekend_All',
        'Call_Outgoing/Incoming_Duration Ratio_Weekend_Evening',
        'Call_Outgoing/Incoming_Duration Ratio_Weekend_Late Night',
        'Call_Outgoing/Incoming_Duration Ratio_Weekend_Morning',
        'Call_Outgoing/Incoming_Duration Ratio_Weekend_Office Hours',
        'SMS_Incoming_Count_Week_All',
        'SMS_Incoming_Count_Week_Evening',
        'SMS_Incoming_Count_Week_Late Night',
        'SMS_Incoming_Count_Week_Morning',
        'SMS_Incoming_Count_Week_Office Hours',
        'SMS_Incoming_Count_Weekday_All',
        'SMS_Incoming_Count_Weekday_Evening',
        'SMS_Incoming_Count_Weekday_Late Night',
        'SMS_Incoming_Count_Weekday_Morning',
        'SMS_Incoming_Count_Weekday_Office Hours',
        'SMS_Incoming_Count_Weekend_All',
        'SMS_Incoming_Count_Weekend_Evening',
        'SMS_Incoming_Count_Weekend_Late Night',
        'SMS_Incoming_Count_Weekend_Morning',
        'SMS_Incoming_Count_Weekend_Office Hours',
        'SMS_Outgoing_Count_Week_All',
        'SMS_Outgoing_Count_Week_Evening',
        'SMS_Outgoing_Count_Week_Late Night',
        'SMS_Outgoing_Count_Week_Morning',
        'SMS_Outgoing_Count_Week_Office Hours',
        'SMS_Outgoing_Count_Weekday_All',
        'SMS_Outgoing_Count_Weekday_Evening',
        'SMS_Outgoing_Count_Weekday_Late Night',
        'SMS_Outgoing_Count_Weekday_Morning',
        'SMS_Outgoing_Count_Weekday_Office Hours',
        'SMS_Outgoing_Count_Weekend_All',
        'SMS_Outgoing_Count_Weekend_Evening',
        'SMS_Outgoing_Count_Weekend_Late Night',
        'SMS_Outgoing_Count_Weekend_Morning',
        'SMS_Outgoing_Count_Weekend_Office Hours',
        'SMS_Outgoing/Incoming_Count Ratio_Week_All',
        'SMS_Outgoing/Incoming_Count Ratio_Week_Evening',
        'SMS_Outgoing/Incoming_Count Ratio_Week_Late Night',
        'SMS_Outgoing/Incoming_Count Ratio_Week_Morning',
        'SMS_Outgoing/Incoming_Count Ratio_Week_Office Hours',
        'SMS_Outgoing/Incoming_Count Ratio_Weekday_All',
        'SMS_Outgoing/Incoming_Count Ratio_Weekday_Evening',
        'SMS_Outgoing/Incoming_Count Ratio_Weekday_Late Night',
        'SMS_Outgoing/Incoming_Count Ratio_Weekday_Morning',
        'SMS_Outgoing/Incoming_Count Ratio_Weekday_Office Hours',
        'SMS_Outgoing/Incoming_Count Ratio_Weekend_All',
        'SMS_Outgoing/Incoming_Count Ratio_Weekend_Evening',
        'SMS_Outgoing/Incoming_Count Ratio_Weekend_Late Night',
        'SMS_Outgoing/Incoming_Count Ratio_Weekend_Morning',
        'SMS_Outgoing/Incoming_Count Ratio_Weekend_Office Hours',
    ],
    'ScreenEventData': [
        'aadhaar_create_session',
        'aadhaar_create_timespent',
        'aadhaar_details_create_session',
        'aadhaar_details_create_timespent',
        'aadhaar_details_update_session',
        'aadhaar_details_update_timespent',
        'aadhaar_update_session',
        'aadhaar_update_timespent',
        'bank_create_session',
        'bank_create_timespent',
        'bank_update_session',
        'bank_update_timespent',
        'documents_create_session',
        'documents_create_timespent',
        'documents_update_session',
        'documents_update_timespent',
        'education_create_session',
        'education_create_timespent',
        'education_update_session',
        'education_update_timespent',
        'eligibility_review_create_session',
        'eligibility_review_create_timespent',
        'eligibility_review_update_session',
        'eligibility_review_update_timespent',
        'finance_create_session',
        'finance_create_timespent',
        'finance_update_session',
        'finance_update_timespent',
        'kyc_review_create_session',
        'kyc_review_create_timespent',
        'kyc_review_update_session',
        'kyc_review_update_timespent',
        'loan_product_create_session',
        'loan_product_create_timespent',
        'loan_product_update_session',
        'loan_product_update_timespent',
        'pan_create_session',
        'pan_create_timespent',
        'pan_update_session',
        'pan_update_timespent',
        'personal_contact_create_session',
        'personal_contact_create_timespent',
        'personal_contact_update_session',
        'personal_contact_update_timespent',
        'profession_create_session',
        'profession_create_timespent',
        'profession_update_session',
        'profession_update_timespent',
        'signup_create_session',
        'signup_create_timespent',
        'signup_update_session',
        'signup_update_timespent',
    ],
    'FieldEventData': [
        'aadhaar_create_current_address_line1_deviation',
        'aadhaar_create_current_address_line1_edits',
        'aadhaar_create_current_address_line2_deviation',
        'aadhaar_create_current_address_line2_edits',
        'aadhaar_create_current_city_deviation',
        'aadhaar_create_current_city_edits',
        'aadhaar_create_current_pincode_deviation',
        'aadhaar_create_current_pincode_edits',
        'aadhaar_create_current_state_deviation',
        'aadhaar_create_current_state_edits',
        'aadhaar_create_dob_deviation',
        'aadhaar_create_dob_edits',
        'aadhaar_create_father_first_name_deviation',
        'aadhaar_create_father_first_name_edits',
        'aadhaar_create_father_last_name_deviation',
        'aadhaar_create_father_last_name_edits',
        'aadhaar_create_first_name_deviation',
        'aadhaar_create_first_name_edits',
        'aadhaar_create_gender_deviation',
        'aadhaar_create_gender_edits',
        'aadhaar_create_last_name_deviation',
        'aadhaar_create_last_name_edits',
        'aadhaar_create_mobile_no_deviation',
        'aadhaar_create_mobile_no_edits',
        'aadhaar_create_mother_first_name_deviation',
        'aadhaar_create_mother_first_name_edits',
        'aadhaar_create_mother_last_name_deviation',
        'aadhaar_create_mother_last_name_edits',
        'aadhaar_create_permanent_address_line1_deviation',
        'aadhaar_create_permanent_address_line1_edits',
        'aadhaar_create_permanent_address_line2_deviation',
        'aadhaar_create_permanent_address_line2_edits',
        'aadhaar_create_permanent_city_deviation',
        'aadhaar_create_permanent_city_edits',
        'aadhaar_create_permanent_pincode_deviation',
        'aadhaar_create_permanent_pincode_edits',
        'aadhaar_create_permanent_state_deviation',
        'aadhaar_create_permanent_state_edits',
        'aadhaar_details_create_account_holder_name_deviation',
        'aadhaar_details_create_account_holder_name_edits',
        'aadhaar_details_create_account_number_deviation',
        'aadhaar_details_create_account_number_edits',
        'aadhaar_details_create_bank_name_deviation',
        'aadhaar_details_create_bank_name_edits',
        'aadhaar_details_create_branch_detail_deviation',
        'aadhaar_details_create_branch_detail_edits',
        'aadhaar_details_create_ifsc_deviation',
        'aadhaar_details_create_ifsc_edits',
        'aadhaar_details_create_upi_mobile_number_deviation',
        'aadhaar_details_create_upi_mobile_number_edits',
        'bank_create_alternate_email_id_deviation',
        'bank_create_alternate_email_id_edits',
        'bank_create_alternate_mob_no_deviation',
        'bank_create_alternate_mob_no_edits',
        'education_create_any_active_loans_deviation',
        'education_create_any_active_loans_edits',
        'education_create_any_owned_vehicles_deviation',
        'education_create_any_owned_vehicles_edits',
        'education_create_dependents_deviation',
        'education_create_dependents_edits',
        'education_create_marital_status_deviation',
        'education_create_marital_status_edits',
        'education_create_profession_type_deviation',
        'education_create_profession_type_edits',
        'education_create_vehicle_type_deviation',
        'education_create_vehicle_type_edits',
        'eligibility_review_create_aadhaar_deviation',
        'eligibility_review_create_aadhaar_edits',
        'eligibility_review_create_office_city_deviation',
        'eligibility_review_create_office_city_edits',
        'eligibility_review_create_salary_deviation',
        'eligibility_review_create_salary_edits',
        'eligibility_review_update_completion_year_deviation',
        'eligibility_review_update_completion_year_edits',
        'eligibility_review_update_qualification_deviation',
        'eligibility_review_update_qualification_edits',
        'finance_create_profession_type_deviation',
        'finance_create_profession_type_edits',
        'finance_create_salary_deviation',
        'finance_create_salary_edits',
        'finance_update_qualification_deviation',
        'finance_update_qualification_edits',
        'loan_product_create_pan_deviation',
        'loan_product_create_pan_edits',
        'pan_create_company_deviation',
        'pan_create_company_edits',
        'pan_create_department_deviation',
        'pan_create_department_edits',
        'pan_create_designation_deviation',
        'pan_create_designation_edits',
        'pan_create_email_deviation',
        'pan_create_email_edits',
        'pan_create_is_phone_no_verified_deviation',
        'pan_create_is_phone_no_verified_edits',
        'pan_create_join_date_deviation',
        'pan_create_join_date_edits',
        'pan_create_nature_of_work_deviation',
        'pan_create_nature_of_work_edits',
        'pan_create_office_city_deviation',
        'pan_create_office_city_edits',
        'pan_create_organisation_type_deviation',
        'pan_create_organisation_type_edits',
        'pan_create_phone_no_deviation',
        'pan_create_phone_no_edits',
        'pan_create_profession_type_deviation',
        'pan_create_profession_type_edits',
        'pan_create_salary_deviation',
        'pan_create_salary_edits',
        'pan_create_salary_payment_mode_deviation',
        'pan_create_salary_payment_mode_edits',
        'pan_create_total_experience_deviation',
        'pan_create_total_experience_edits',
        'personal_contact_create_document_type_deviation',
        'personal_contact_create_document_type_edits',
        'profession_create_college_deviation',
        'profession_create_college_edits',
        'profession_create_completion_year_deviation',
        'profession_create_completion_year_edits',
        'profession_create_qualification_deviation',
        'profession_create_qualification_edits',
        'profession_create_qualification_type_deviation',
        'profession_create_qualification_type_edits',
        'signup_create_existing_emi_deviation',
        'signup_create_existing_emi_edits',
        'signup_create_loan_amount_deviation',
        'signup_create_loan_amount_edits',
        'signup_create_loan_emi_deviation',
        'signup_create_loan_emi_edits',
        'signup_create_loan_purpose_deviation',
        'signup_create_loan_purpose_edits',
        'signup_create_loan_tenure_deviation',
        'signup_create_loan_tenure_edits',
    ],
}
