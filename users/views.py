from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from .models import CustomUser
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('registration_confirmation', user_id=user.id)
    else:
        form = UserRegistrationForm()
    return render(request, 'users/signup.html', {'form': form})

def registration_confirmation(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'users/registration_confirmation.html', {'user': user})



@require_http_methods(["POST"])
def check_email(request):
    email = request.POST.get('email', '')
    exists = CustomUser.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})


@csrf_protect
@require_http_methods(["POST"])
def validate_field(request):
    field_name = request.POST.get('field')
    value = request.POST.get('value')
    
    if not field_name or value is None:
        return JsonResponse({'error': 'Missing parameters'}, status=400)
    form_data = {field_name: value}
    
    if field_name == 'repeat_password':
        form_data['password'] = request.POST.get('password', '')
    form = UserRegistrationForm(form_data)
    
    form.is_valid()
    
    return JsonResponse({
        'valid': field_name not in form.errors,
        'field': field_name
    })


def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})