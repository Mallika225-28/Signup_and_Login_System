from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            Profile.objects.create(
                user=user,
                user_type=form.cleaned_data['user_type'],
                profile_picture=form.cleaned_data['profile_picture'],
                address_line1=form.cleaned_data['address_line1'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode']
            )
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if user.profile.user_type == 'patient':
                    return redirect('patient_dashboard')
                else:
                    return redirect('doctor_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def patient_dashboard(request):
    profile = request.user.profile
    return render(request, 'patient_dashboard.html', {'profile': profile})

def doctor_dashboard(request):
    profile = request.user.profile
    return render(request, 'doctor_dashboard.html', {'profile': profile})
