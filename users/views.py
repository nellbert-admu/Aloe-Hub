from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from events.models import Event
from events.views import quick_sort  # Import the quick_sort function

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    messages.success(request, 'You have logged out successfully!')
    return redirect('home')  # Redirect to login page after successful logout

def home(request):
    context = {}
    if request.user.is_authenticated:
        favorited_events = request.user.favorited_events.all()
        context['favorited_events'] = quick_sort(list(favorited_events), 'date')  # Sort by date
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')