from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('validate-field/', views.validate_field, name='validate_field'),
    path('registration-confirmation/<int:user_id>/', 
         views.registration_confirmation, 
         name='registration_confirmation'),
    path('check-email/', views.check_email, name='check_email'),
]