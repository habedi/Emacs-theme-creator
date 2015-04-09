from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


#def index(request):
#    return HttpResponse("i'm going to show you the world on!.")

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
