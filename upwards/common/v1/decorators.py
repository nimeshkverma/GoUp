import logging
from functools import wraps
from django.db import IntegrityError
from django.conf import settings
from rest_framework import status
from serializers import AuthenticationSerializer
from response import MetaDataResponse
from exceptions import NotAcceptableError, ConflictError


def session_authorize(customer_id_key='pk', *args, **kwargs):
    def deco(f):
        def abstract_customer_id(request):
            if request.method == 'GET':
                customer_id = request.query_params.get(customer_id_key)[0]
            else:
                customer_id = request.data.get(customer_id_key)
            return customer_id

        def abstract_session_token(request):
            session_token_header_key = 'HTTP_SESSION_TOKEN'
            return request.META.get(session_token_header_key)

        @wraps(f)
        def decorated_function(*args, **kwargs):
            request = args[1]
            if kwargs.get(customer_id_key):
                customer_id = kwargs[customer_id_key]
                kwargs.pop(customer_id_key)
            else:
                customer_id = abstract_customer_id(request)
            auth_data = {
                'customer_id': customer_id,
                'session_token': abstract_session_token(request)
            }
            auth_serializer = AuthenticationSerializer(data=auth_data)
            auth_data['authorized'] = auth_serializer.is_valid(
            ) and auth_serializer.verify_and_update_session()
            return f(auth_data=auth_data, *args, **kwargs)
        return decorated_function
    return deco


def default_logger():
    logger = logging.getLogger("From the Decorator file")
    return logger


def catch_exception(LOGGER=default_logger()):
    def deco(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except NotAcceptableError as e:
                LOGGER.error("NotAcceptableError:%s" % str(e))
                return MetaDataResponse(e.response, e.meta, status=e.status)
            except ConflictError as e:
                LOGGER.error("MetaDataRresponse:%s" % str(e))
                return MetaDataResponse(e.response, e.meta, status=e.status)
            except IntegrityError as e:
                LOGGER.error("IntegrityError:%s" % str(e))
                return MetaDataResponse({}, str(e), status=status.HTTP_409_CONFLICT)
            except Exception as e:
                LOGGER.error("Encountered Exception%s" % str(e))
                return MetaDataResponse({}, str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return decorated_function
    return deco


def meta_data_response(meta=""):
    def deco(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            vanilla_response = f(*args, **kwargs)
            return MetaDataResponse(vanilla_response.data, meta, status=vanilla_response.status_code)
        return decorated_function
    return deco


def thirdparty_authorize():
    def deco(f):
        def abstract_session_token(request):
            session_token_header_key = 'HTTP_SESSION_TOKEN'
            return request.META.get(session_token_header_key)

        @wraps(f)
        def decorated_function(*args, **kwargs):
            third_party_auth = False
            third_party = kwargs.get('third_party')
            third_party_token = abstract_session_token(args[1])
            if settings.THIRTY_PARTY_SECRETS.get(third_party) == third_party_token:
                third_party_auth = True
            return f(third_party_auth=third_party_auth, *args, **kwargs)
        return decorated_function
    return deco
