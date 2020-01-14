from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .forms import UploadFileForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_success')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', { 'form': form })


def upload_image(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():            
            usr = CustomUser.objects.get(email=request.user)
            usr.profile_image = request.FILES['imagefile']
            usr.save()
            return redirect('user_profile')
    else:
        form = UploadFileForm()
    return render(request, 'LandingPage.html', { 'form': form })
