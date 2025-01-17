from django.shortcuts import render

# Create your views here.


def hello(request):
    context = {
        "message": "Hello, world!",
    }
    return render(request, "pyhackregister/hello.html", context)
