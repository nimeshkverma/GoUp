from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from participant import models

from common.v1.decorators import session_authorize, meta_data_response, catch_exception
from analytics.v1.services.credit_service import CustomerCreditLimit
from activity.models import register_customer_state
from activity.model_constants import ELIGIBILITY_SUBMIT_STATE

import logging
LOGGER = logging.getLogger(__name__)


class BorrowerCreate(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize('customer_id')
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            customer_credit_limit = CustomerCreditLimit(
                auth_data['customer_id'])
            data = {
                'credit_limit': customer_credit_limit.limit,
            }
            data.update(request.data)
            data['eligible_for_loan'] = customer_credit_limit.is_eligible
            serializer = serializers.BorrowerSerializer(
                data=data)
            if not serializer.is_valid():
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            if not data['eligible_for_loan']:
                register_customer_state(
                    ELIGIBILITY_SUBMIT_STATE, auth_data['customer_id'])
                return Response(data, status=status.HTTP_200_OK)

            serializer.validate_foreign_keys()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({}, status.HTTP_401_UNAUTHORIZED)


class BorrowerDetail(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    def get(self, request, pk):
        borrower_object = get_object_or_404(
            models.Borrower, customer_id=pk)
        serializer = serializers.BorrowerSerializer(
            borrower_object)
        return Response(serializer.data, status.HTTP_200_OK)

    @catch_exception(LOGGER)
    @meta_data_response()
    def put(self, request, pk):
        borrower_object = get_object_or_404(
            models.Borrower, customer_id=pk)
        serializers.BorrowerSerializer().validate_foreign_keys(request.data)
        borrower_object_updated = serializers.BorrowerSerializer().update(
            borrower_object, request.data)
        return Response(serializers.BorrowerSerializer(borrower_object_updated).data, status.HTTP_200_OK)

    @catch_exception(LOGGER)
    @meta_data_response()
    def delete(self, request, pk):
        borrower_object = get_object_or_404(
            models.Borrower, customer_id=pk)
        borrower_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LenderList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = models.Lender.active_objects.all()
    serializer_class = serializers.LenderSerializer

    @catch_exception(LOGGER)
    @meta_data_response()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @catch_exception(LOGGER)
    @meta_data_response()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LenderDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = models.Lender.objects.all()
    serializer_class = serializers.LenderSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
