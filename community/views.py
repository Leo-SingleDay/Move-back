from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.views.decorators.http import require_safe
from .models import Comment, Review

@require_safe
def index(request):
    pass

