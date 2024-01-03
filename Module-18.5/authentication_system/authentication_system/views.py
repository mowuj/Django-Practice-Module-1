from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        register_form=forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Registration Successfully Done")
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html',{'form':register_form,'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Login successful')
                login(request,user)
                return redirect('profile')
            else:
                messages.error(request,'Login Information Invalid')
                return redirect('login')
    else:
        form=AuthenticationForm()
    return render(request,'register.html',{'form':form,'type':'Login'})

@login_required()
def profile(request):
    return render(request,'profile.html')


@login_required()
def change_pass(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password changed successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html',{'form':form})


@login_required()
def user_logout(request):
    logout(request)
    return redirect('login')