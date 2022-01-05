from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first(request):

    return HttpResponse('unouno')

def second(request):
    return HttpResponse('dosdos')