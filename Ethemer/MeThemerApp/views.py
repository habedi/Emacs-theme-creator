from django.shortcuts import render


def index(request):
    return HttpResponse("i'm going to show you the world on!.")
