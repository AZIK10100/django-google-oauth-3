from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from googleauth.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    return render(request, 'index.html')


def login_page(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        # Add the backend attribute here
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)  
        return redirect('index')

    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add the backend attribute here
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})
    

def logout_page(request):
    logout(request)
    return redirect('login_page')