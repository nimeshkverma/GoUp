from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from loan_product import models
from common.v1.decorators import session_authorize, meta_data_response, catch_exception
from activity.models import register_customer_state
from activity.model_constants import ELIGIBILITY_REJECTED_LOAN_PRODUCT_SUBMIT_STATE, LOAN_SPECIFICATION_REVIEW_STATE

import logging
LOGGER = logging.getLogger(__name__)


class LoanProductCreate(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize('customer_id')
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            serializer = serializers.LoanProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validate_foreign_keys()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status.HTTP_401_UNAUTHORIZED)


class LoanProductDetail(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize()
    def get(self, request, auth_data, *args, **kwargs):
        if auth_data.get('authorized'):
            loan_product_object = get_object_or_404(
                models.LoanProduct, customer_id=auth_data['customer_id'])
            serializer = serializers.LoanProductSerializer(loan_product_object)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({}, status.HTTP_401_UNAUTHORIZED)

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize()
    def put(self, request, auth_data, *args, **kwargs):
        if auth_data.get('authorized'):
            loan_product_object = get_object_or_404(
                models.LoanProduct, customer_id=auth_data['customer_id'])
            serializers.LoanProductSerializer().validate_foreign_keys(request.data)
            loan_product_object_updated = serializers.LoanProductSerializer().update(
                loan_product_object, request.data)
            register_customer_state(
                ELIGIBILITY_REJECTED_LOAN_PRODUCT_SUBMIT_STATE, auth_data['customer_id'])
            return Response(serializers.LoanProductSerializer(loan_product_object_updated).data, status.HTTP_200_OK)
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize()
    def delete(self, request, auth_data, *args, **kwargs):
        if auth_data.get('authorized'):
            loan_product_object = get_object_or_404(
                models.LoanProduct, customer_id=auth_data['customer_id'])
            loan_product_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({}, status.HTTP_401_UNAUTHORIZED)


class LoanSpecifications(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize()
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            dummy = {
                "principal_amount": 10000,
                "tenure": 20,
                "emi": 550,
            }
            register_customer_state(
                LOAN_SPECIFICATION_REVIEW_STATE, auth_data['customer_id'])
            return Response(dummy, status=status.HTTP_200_OK)
        return Response({}, status.HTTP_401_UNAUTHORIZED)
