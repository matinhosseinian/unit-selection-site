from django.urls import reverse_lazy
from django.views import generic, View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import CustomUserCreationForm, LoginForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
    

class UserLoginView(View):

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    def get(self, request):
        form = LoginForm()
        return render(request, "registration/login.html", {"form": form})
    
def UserLogout(request):
    logout(request)
    return redirect("home")