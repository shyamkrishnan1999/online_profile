# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'portal/homepage.html',{})


def login_go(request):
    return render(request,'portal/login.html',{})

def sign_up(request):
    return render(request,'portal/signup.html',{})
