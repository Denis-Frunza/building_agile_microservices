from django.urls import include, path
from dj_rest_auth.registration.views import  ConfirmEmailView, VerifyEmailView
from allauth.account.views import EmailView, LogoutView, LoginView, SignupView, PasswordResetView

from . import views



urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/register/verify-email/', EmailView.as_view(), name='account_email'),
    path('api/auth/register/account-confirm-email/<str:key>/',ConfirmEmailView.as_view(),),  # Needs to be defined before the registration path
    path('api/auth/register/account-confirm-email/', VerifyEmailView.as_view(),name='account_email_verification_sent'),
    path('api/auth/register/', include('dj_rest_auth.registration.urls')),
    path('api/auth/register/', SignupView.as_view(), name='account_signup'),
    path('api/auth/login/', LoginView.as_view(), name='account_login'),
    path('api/auth/logout/', LogoutView.as_view(), name='account_logout'),
    path('api/auth/password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('api/auth/profile/<int:pk>/', views.UserProfile.as_view(), name='account_profile')

]
