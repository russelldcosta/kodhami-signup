from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from .models import CustomUser

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