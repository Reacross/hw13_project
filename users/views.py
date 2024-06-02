from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RegisterForm

# Create your views here.

class RegisterView(View):

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect(to="quotes:root")
        return super().dispatch(request, *args, **kwargs)
    

    template_name = 'users/register.html'
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            usernames = form.cleaned_data["username"]
            messages.success(request, f'Account created for {usernames}')
            return redirect(to="users:signin")
        return render(request, self.template_name, {'form': form})
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'