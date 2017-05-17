from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import LoginForm, SignupForm


def check_login_status(request):
    if not request.user.is_authenticated():
        return redirect('main:index')


class Index(View):

    def get(self, request, *args, **kwargs):
        loginForm = LoginForm()
        signupForm = SignupForm()
        context_data = {
            'loginForm': loginForm,
            'signupForm': signupForm
        }
        return render(request, 'index.html', context_data)


class Login(View):
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        loginForm = self.form_class(request.POST or None)
        signupForm = SignupForm()
        context_data = {
            'loginForm': loginForm,
            'signupForm': signupForm
        }
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            user = User.objects.get(username=username)
            if not user.is_active:
                context_data['msg_err'] = 'Please verify your email before logging in.'
                return render(request, 'index.html', context_data)
            user = authenticate(username=username, password=password)
            if user is None:
                context_data['msg_err'] = 'Invalid Credentials.'
                return render(request, 'index.html', context_data)
            else:
                login(request, user)
                return redirect('main:profile')

        context_data['msg_err'] = 'Details Not Valid'
        return render(request, 'index.html', context_data)


class Signup(View):
    form_class = SignupForm

    def post(self, request, *args, **kwargs):
        signupForm = self.form_class(request.POST or None)
        loginForm = LoginForm()
        context_data = {
            'loginForm': loginForm,
            'signupForm': signupForm
        }
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            password = signupForm.cleaned_data['password']
            user.set_password(password)
            user.is_active = False
            user.save()
            try:
                send_mail('Verify Your Email', "Welcome to my website.Please click <a href='http://127.0.0.1:8000/activate/{}'>here</a> to verify your email".format(user.id),
                          'jack.sparo435@gmail.com',
                          [user.email],
                          fail_silently=False,)
            except:
                return HttpResponse('Problem sending verification email')

            context_data['msg_suc'] = 'Registration Successful'
            return render(request, 'index.html', context_data)

        context_data['msg_err'] = 'Details Not Valid'
        return render(request, 'index.html', context_data)


class Profile(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect(settings.LOGIN_URL)
        return render(request, 'profile.html', {'user': request.user})


def email(request):
    # try:
    send_mail('Djano mail',
              'Hello email from django.',
              'jack.sparo435@gmail.com',
              ['jack.sparo435@gmail.com'],
              fail_silently=False,)
    # except:
    #     return HttpResponse("Email Failed to Send")

    return HttpResponse("Email Sent Successfully")


def activate(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return render(request, 'activate.html', {'msg': '<h3>Email verified<br/>Click <a href="/">here</a> to login</h3>'})


def logmeout(request):
    logout(request)
    return redirect('main:index')
