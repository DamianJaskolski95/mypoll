from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. It's index page.")
