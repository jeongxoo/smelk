from django.shortcuts import render

def pages(request):
    return render(
        request,
        "main_page/index.html"
    )