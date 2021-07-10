from django.shortcuts import render

# Create your views here.



from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render, redirect
from django.views.generic import RedirectView


def login(request):
    if not request.user.is_authenticated:
        return render(request, 'web3auth/login.html')
    else:
        return redirect('/admin/login')


def auto_login(request):
    if not request.user.is_authenticated:
        return render(request, 'web3auth/autologin.html')
    else:
        return redirect('/admin/login')


def index (request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/admin/login')
