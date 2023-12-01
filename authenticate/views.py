from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views import View
from .forms import FormLogin
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginView(View):
    template_name = "registration/login.html"

    def get(self, request):
        context = {'form_login': FormLogin()}
        return render(request, "registration/login.html", context)

    def post(self, request):
        usuario = authenticate(
            request, email=request.POST['email'], password=request.POST['password'])
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            context = {"error": "User not found",
                'form_login': FormLogin()}
            print(context)
            return render(request, 'registration/login.html', context)