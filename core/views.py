from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('email')
            user.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user is not None:
                login(request, user)
                return redirect('main')  # Redirect to main functionality after login
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required(login_url='login')
def main(request):
    """
    Display the main page with the YouTube URL input.
    """
    return render(request, 'main.html')

@login_required(login_url='login')
def generate_blog(request):
    """
    Handle YouTube URL submission and generate blog content.
    """
    if request.method == 'POST':
        youtube_url = request.POST.get('youtube_url')
        if youtube_url:
            # Here you can integrate your AI or blog generation logic
            generated_blog = f"This is a generated blog for the YouTube URL: {youtube_url}"
            return render(request, 'main.html', {'blog': generated_blog})
        else:
            messages.error(request, "Please enter a valid YouTube URL.")
            return redirect('main')
    else:
        return redirect('main')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request, "profile.html")

def about(request):
    return render(request, "about.html")
