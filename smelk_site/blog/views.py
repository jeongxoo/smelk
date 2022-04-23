import re
from django.shortcuts import render
from django.http import HttpResponse

def mainp(request):
    return render(
        request,
        "blog/main.html"
    )