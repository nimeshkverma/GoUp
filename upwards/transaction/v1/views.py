from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from rest_framework.response import Response


from . import serializers
from transaction import models

from common.v1.decorators import meta_data_response, catch_exception, session_authorize

import logging
LOGGER = logging.getLogger(__name__)


class TransactionHistoryDetails(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize()
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            serializer = serializers.TransactionHistoryDetailsSerializer(
                data={'customer_id': auth_data['customer_id']})
            if serializer.is_valid():
                transaction_history = serializer.get_transaction_history()
                if transaction_history:
                    return Response(transaction_history, status=status.HTTP_200_OK)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status.HTTP_401_UNAUTHORIZED)
