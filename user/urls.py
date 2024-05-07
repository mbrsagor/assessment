from django.urls import path
from user import views

urlpatterns = [
    path('signin/', views.SignInAPIView.as_view()),
    path('signup/', views.RegistrationAPIView.as_view()),
    path('signout/', views.SignOutAPIView.as_view()),
    path('password-change/<pk>/', views.PasswordChangeAPI.as_view()),
    path('profile/', views.UserProfileAPIView.as_view()),
    path('profile/<pk>/', views.UserProfileUpdateView.as_view()),
]
