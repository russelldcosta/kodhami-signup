from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('registration-confirmation/<int:user_id>/', views.registration_confirmation, name='registration_confirmation'),
]