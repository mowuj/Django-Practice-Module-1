from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UserUpdateForm
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self,form):
        
        user=form.save()
        login(self.request,user)
        
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name='accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):        
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
class UserBankAccountUpdateView(View):
    template_name='accounts/profile.html'

    def get(self,request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self,request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
        return render(request, self.template_name, {'form': form})


def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed Successfully')
            update_session_auth_hash(request, form.user)
            
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_pass.html', {'form': form})
