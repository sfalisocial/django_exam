from django.shortcuts import render, redirect
from django.contrib import messages
from ..logreg.models import User
from datetime import datetime, date


def index(request):
    return render(request,'exam/index.html')
