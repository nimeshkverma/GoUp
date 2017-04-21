VAHAN_API_MODEL_MAPPING = {
    "registrationNo": "registration_no",
    "make": "make",
    "model": "model",
    "makeModel": "make_model",
    "fuel": "fuel",
    "displayVariant": "display_variant",
    "shortVariant": "short_variant",
    "vehicleId": "vehicle_id",
    "vertical": "vertical",
    "registrationDate": "registration_date",
}

VAHAN_API_MODEL_RTO_MAPPING = {
    "rtoCode": "rto_code",
    "lntLoc": "rto_lnt_location",
    "rtoPlateLntLoc": "rto_plate_lnt_location"
}

LOAN_INTEREST_RATE = {
    'default': 0.03
}

LOAN_PROCCESSING_FEES = {
    'nsdl_failed': {
        'principal_percent': 2,
        'minimum': 700,
        'maximum': 2000,
    },
    'nsdl_success': {
        'principal_percent': 2,
        'minimum': 500,
        'maximum': 2000,
    },

}

LOAN_PENALTY_RATE_PER_TENURE = 0.03
