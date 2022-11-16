from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


