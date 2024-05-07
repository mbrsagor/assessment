from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler
from django.http import JsonResponse


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)
    # checks if the raised exception is of the type you want to handle
    if isinstance(exc, ValidationError):
        # defines custom response data
        err_data = {'status': False, 'message': f'{exc}'}
        return JsonResponse(err_data, safe=False, status=200)
    return response
