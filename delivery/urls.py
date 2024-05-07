from django.urls import path

from delivery import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
]
