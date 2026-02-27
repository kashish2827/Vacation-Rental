from django.shortcuts import render, redirect
from .forms import UserSignForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings

def userSignupView(request):
    if request.method == "POST":
        form = UserSignForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            send_mail(subject='Welcome to Vacation Rental',message='Thank you for signing up for our vacation rental service! We are excited to have you on board and look forward to helping you find the perfect vacation rental for your next trip.',from_email=settings.EMAIL_HOST_USER,recipient_list=[email],fail_silently=False)
            form.save()
            return redirect('login')
        else:
            return render(request, 'core/signup.html', {'form': form})
    else:
        form = UserSignForm()
        return render(request, 'core/signup.html', {'form': form})


def UserLoginView(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']            
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)

                if user.role == 'host':
                    return redirect('host_dashboard')
                elif user.role == 'user':
                    return redirect('user_dashboard')
                elif user.role == 'admin':
                    return redirect('/admin/')

        # VERY IMPORTANT — return if invalid
        return render(request, 'core/login.html', {'form': form})

    else:
        form = UserLoginForm()
        return render(request, 'core/login.html', {'form': form})