from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from .forms import CustomUserCreationForm
class HomeView(View):
    def get(self, request):
        return render(request, 'users/home.html')
class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change to your desired redirect URL after registration
        return render(request, 'users/register.html', {'form': form})

from django.contrib.auth import views as auth_views

class CustomLoginView(auth_views.LoginView):
    template_name = 'users/login.html'


class CustomLogoutView(LogoutView):
    next_page = 'home'