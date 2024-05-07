def prepare_create_success_response():
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': 'Data Successfully created',
    }
    return response


def password_change_success_response():
    response = {
        'status': True,
        'message': 'Password changed successfully.',
    }
    return response


def password_change_failed_response():
    response = {
        'status': False,
        'message': 'old password is wrong',
    }
    return response


def auth_success_response(message):
    response = {
        'status': True,
        'message': message,
    }
    return response


def auth_failed_response(message):
    response = {
        'status': False,
        'message': message,
    }
    return response


def prepare_success_response(serializer_data):
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': 'Data successfully returned',
        'data': serializer_data
    }
    return response


def profile_success_response(serializer_data):
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': 'Profile successfully returned',
        'profile': serializer_data
    }
    return response


def prepare_error_response(serializer_error):
    """ prepare error response for all serializer """
    response = {
        'status': False,
        'message': serializer_error
    }
    return response


def prepare_generic_error(error_code, details):
    """
    method for build generic error
    @param error_code: error_code should be provided by this param
    @param details: error message
    :return:
    """
    response = {
        "status": 'error',
        "message": details,
        "data": None
    }
    return response
