from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import views, generics, status, permissions

# from utils import otp
from user.models import User
from user import serializers
from utils import response
from utils import message


# User Login API
class SignInAPIView(ObtainAuthToken):
    """
    Name: User SignIn API
    URL: /api/v1/user/signin/
    """
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
            user = serializer.validated_data['user']
            device_token = request.data['device_token']
            try:
                user.device_token += device_token
                # print(user.device_token)
                user.save()
            except AttributeError as ex:
                return Response(response.prepare_error_response(str(ex)))
            return Response({
                'uuid': user.uuid,
                'status': True,
                'role': user.role,
                'message': message.SIGNIN,
                'device_token': user.device_token,
                'token': token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response(response.auth_failed_response(message.SIGNIN_FAILED), status=status.HTTP_200_OK)


# class SignUpAPIView(views.APIView):
#     """
#     Name: User signUp API
#     URL: /api/v1/user/signup/
#     :param
#     name, email, phone, password
#     """
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request):
#         try:
#             serializer = serializers.UserSignUpSerializer(data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 user = serializer.save()
#                 # Send OTP
#                 otp = otp_utils.generate_otp()
#                 user.otp = otp
#                 user.is_active = False
#                 user.save()
#                 otp_utils.send_otp_account_activate(user.email, user.otp)
#                 return Response(response.prepare_create_success_response(messages.SIGNUP_SUCCESS),
#                                 status=status.HTTP_201_CREATED)
#             error_list = [serializer.errors[error][0] for error in serializer.errors]
#             error = ' '.join(error_list)
#             return Response(response.prepare_error_response(error), status=status.HTTP_200_OK)
#         except Exception as ex:
#             return Response(response.prepare_error_response(str(ex)), status=status.HTTP_200_OK)


class RegistrationAPIView(views.APIView):
    """
    Name: User SignUp API
    URL: /api/v1/user/signup/
    """
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        try:
            data = request.data
            full_name = data['full_name']
            phone = data['phone']
            email = data['email']
            email = email.lower()
            password = data['password']
            re_password = data['re_password']
            if password == re_password:
                if len(password) >= 8:
                    if User.objects.filter(email=email).exists():
                        return Response(response.auth_failed_response(message.EMAIL_EXISTS),
                                        status=status.HTTP_200_OK)
                    elif User.objects.filter(phone=phone).exists():
                        return Response(response.auth_failed_response(message.PHONE_EXISTS),
                                        status=status.HTTP_200_OK)
                    else:
                        User.objects.create_user(full_name=full_name, email=email, phone=phone, password=password)
                        return Response(response.auth_success_response(message.SIGNUP), status=status.HTTP_201_CREATED)
                else:
                    return Response(response.auth_failed_response(message.PASSWORD_VALIDATE),
                                    status=status.HTTP_200_OK)
            else:
                return Response(response.auth_failed_response(message.PASSWORD_MATCH),
                                status=status.HTTP_200_OK)

        except Exception as ex:
            print(ex)
            return Response(response.auth_failed_response(message.REGISTRATION_ERROR),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PasswordChangeAPI(generics.UpdateAPIView):
    """
    Name: User password change API
    URL: /api/v1/user/change-password/pk/
    """
    queryset = User
    serializer_class = serializers.PasswordChangeSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(response.password_change_failed_response(), status=status.HTTP_200_OK)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(response.password_change_success_response(), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)


class UserProfileAPIView(views.APIView):
    """
    Name: User Profile API for Web mobile both
    URL: /api/v1/user/profile/
    """

    def get(self, request, **kwargs):
        try:
            user = User.objects.get(id=self.request.user.id)
            if user is not None:
                serializer = serializers.UserSerializer(user)
                return Response(response.profile_success_response(serializer.data), status=status.HTTP_200_OK)
            return Response(response.prepare_error_response("The user ID not found."), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(response.prepare_error_response(str(ex)), status=status.HTTP_200_OK)


class UserProfileUpdateView(views.APIView):
    """
    Name: User Profile update API for Web mobile both
    URL: /api/v1/user/profile/<pk>/
    """

    def get_object(self, pk):
        try:
            return User.objects.filter(id=pk).first()
        except User.DoesNotExist:
            return None

    def put(self, request, pk):
        user = self.get_object(pk)
        if user is not None:
            serializer = serializers.UserProfileUpdateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save(user=self.request.user)
                return Response(response.auth_success_response(message.PROFILE_UPDATE), status=status.HTTP_201_CREATED)
            error_list = [serializer.errors[error][0] for error in serializer.errors]
            error = ' '.join(error_list)
            return Response(response.auth_failed_response(error), status=status.HTTP_200_OK)
        else:
            return Response(response.auth_failed_response(message.PROFILE_ERROR), status=status.HTTP_200_OK)


# Sign Out
class SignOutAPIView(views.APIView):
    """
    Name: User SignOut API
    URL: /api/v1/user/signout/
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, format=None):
        # simply delete the token to force a login
        if request.user.auth_token:
            try:
                device_token = ""
                user = User.objects.update(device_token=device_token)
                print(user)
            except Exception as ex:
                print(str(ex))
            request.user.auth_token.delete()
            return Response(response.auth_success_response(message.SIGNOUT), status=status.HTTP_200_OK)
        else:
            return Response(response.prepare_error_response(message.EXPIRED))
