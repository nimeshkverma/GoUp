import json
from copy import deepcopy
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from common.v1.decorators import session_authorize, meta_data_response, catch_exception
from analytics import models

from . import serializers

import logging
LOGGER = logging.getLogger(__name__)


class Algo360DataDetails(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize('customer_id')
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            serializer = serializers.Algo360DataSerializer(
                data=request.data)
            if serializer.is_valid():
                serializer.validate_foreign_keys()
                return Response(serializer.store_algo360_data(), status.HTTP_200_OK)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status.HTTP_401_UNAUTHORIZED)


class CreditReportDetails(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    def get(self, request, pk, *args, **kwargs):
        data = {'customer_id': pk}
        serializer = serializers.CreditReportSerializer(data=data)
        if serializer.is_valid():
            serializer.validate_foreign_keys()
            return Response(serializer.report_data(), status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DataLogCreate(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize('customer_id')
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            data = deepcopy(request.data)
            log_data = json.dumps(data.pop('log_data'))
            data['log_data'] = log_data
            serializer = serializers.DataLogSerializer(data=data)
            if serializer.is_valid():
                serializer.validate_foreign_keys()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status.HTTP_401_UNAUTHORIZED)


class DataLogDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = models.DataLog.objects.all()
    serializer_class = serializers.DataLogSerializer

    @catch_exception(LOGGER)
    @meta_data_response()
    @session_authorize()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# class DataLogDetail(APIView):

#     # @catch_exception(LOGGER)
#     @meta_data_response()
#     @session_authorize()
#     def get(self, request, auth_data, *args, **kwargs):
#         if auth_data.get('authorized'):
#             datalog_object = get_object_or_404(
#                 models.DataLog, customer_id=auth_data['customer_id'])
#             serializer = serializers.DataLogSerializer(datalog_object)
#             return Response(serializer.data, status.HTTP_200_OK)
#         return Response({}, status.HTTP_401_UNAUTHORIZED)

    # @catch_exception(LOGGER)
    # @meta_data_response()
    # @session_authorize()
    # def put(self, request, auth_data, *args, **kwargs):
    #     if auth_data.get('authorized'):
    #         datalog_object = get_object_or_404(
    #             models.DataLog, customer_id=auth_data['customer_id'])
    #         serializers.DataLogSerializer().validate_foreign_keys(request.data)
    #         datalog_object_updated = serializers.DataLogSerializer().update(
    #             datalog_object, request.data)
    #         return Response(serializers.DataLogSerializer(datalog_object_updated).data, status.HTTP_200_OK)
    #     return Response({}, status=status.HTTP_401_UNAUTHORIZED)

    # @catch_exception(LOGGER)
    # @meta_data_response()
    # @session_authorize()
    # def delete(self, request, auth_data, *args, **kwargs):
    #     if auth_data.get('authorized'):
    #         datalog_object = get_object_or_404(
    #             models.DataLog, customer_id=auth_data['customer_id'])
    #         datalog_object.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     return Response({}, status.HTTP_401_UNAUTHORIZED)
