from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from rest_framework.response import Response


from . import serializers
from transaction import models

from common.v1.decorators import meta_data_response, catch_exception, session_authorize

import logging
LOGGER = logging.getLogger(__name__)


class RepaymentDetails(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize()
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            data = {
                "next_emi_amount": 2345,
                "next_emi_due_date": "2017-05-26",
                "past_emi_due": 4690,
                "late_payment_penalty": 1000,
                "total_payment_due": 5690,
                "all_payment_due": 8035
            }
            return Response(data, status.HTTP_200_OK)
        return Response({}, status.HTTP_401_UNAUTHORIZED)


class RepaymentSchedule(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize()
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            data = {
                "loan_amount": 20000,
                "loan_interest": 0.03,
                "number_of_emi": 10,
                "tenure": 10,
                "customer_id": "23",
                "emi": 2345,
                "processing_fee": 500,
                "no_of_emi_paid": 4,
                "repayment_profile": [
                    {
                        "due_date": "2017-09-26",
                        "serial_no": 1,
                        "emi": 2345,
                        "principal_outstanding": 12702,
                        "principal_paid": 1964,
                        "interest_paid": 382
                    },
                    {
                        "due_date": "2017-10-26",
                        "serial_no": 2,
                        "emi": 2345,
                        "principal_outstanding": 10738,
                        "principal_paid": 2023,
                        "interest_paid": 323
                    },
                    {
                        "due_date": "2017-11-26",
                        "serial_no": 3,
                        "emi": 2345,
                        "principal_outstanding": 8716,
                        "principal_paid": 2084,
                        "interest_paid": 262
                    },
                    {
                        "due_date": "2017-12-26",
                        "serial_no": 4,
                        "emi": 2345,
                        "principal_outstanding": 6632,
                        "principal_paid": 2146,
                        "interest_paid": 199
                    },
                    {
                        "due_date": "2018-01-26",
                        "serial_no": 5,
                        "emi": 2345,
                        "principal_outstanding": 4487,
                        "principal_paid": 2211,
                        "interest_paid": 135
                    },
                    {
                        "due_date": "2018-02-26",
                        "serial_no": 6,
                        "emi": 2345,
                        "principal_outstanding": 2277,
                        "principal_paid": 2277,
                        "interest_paid": 69
                    }
                ],
            }
            return Response(data, status.HTTP_200_OK)
        return Response({}, status.HTTP_401_UNAUTHORIZED)


class TransactionHistoryDetails(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize()
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            data = {
                "transaction_history": [
                    {
                        "loan_id": 1,
                        "installment_id": 1,
                        "amount": 10000,
                        "utr": "1234",
                        "transaction_status": "initiated",
                        "transaction_type": "loan_avail",
                        "status_actor": "upwards",
                        "created_at": "2017-05-01",
                        "updated_at": "2017-05-02"
                    }
                ]
            }
            return Response(data, status.HTTP_200_OK)
        return Response({}, status.HTTP_401_UNAUTHORIZED)
