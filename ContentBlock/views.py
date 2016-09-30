from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import loader
from django.views.generic import TemplateView


def hello(request):
    return HttpResponse(loader.get_template("hello.html").render())

def momo(request):
    return render_to_response('base.html')
