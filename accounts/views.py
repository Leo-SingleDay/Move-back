from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm


@require_http_methods(['GET', 'POST'])
def signup(request):
    pass

@require_http_methods(['GET', 'POST'])
def login(request):
    pass

@require_POST
def logout(request):
    pass