from django.conf import settings
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from .forms import FormLogin, SignUpForm

User = get_user_model()

@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

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

class RegisterView(View):
    
    def get(self, request):
        form_signup = SignUpForm()
        context = {'form_signup': form_signup}
        template_name = 'registration/signup.html'
        return render(request, template_name, context)

    def post(self, request):
        form_signup = SignUpForm(data=request.POST)
        if form_signup.is_valid():
            random_pass = User.objects.make_random_password(
                length=8, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            )
            user = User.objects.create_user(
                username = form_signup.cleaned_data['username'],
                email = form_signup.cleaned_data['email'],
                password = random_pass
            )
            user.is_active = True
            user.save()
            send_mail(
                'Your Bookstore password',
                'Welcome to Bookstore, your password is: ' + random_pass,
                settings.EMAIL_HOST_USER,
                (user.email,),
                fail_silently=False,
            )
            return redirect('login')
        else:
            context = {'form_signup': form_signup}
            return render(request, 'registration/signup.html', context)