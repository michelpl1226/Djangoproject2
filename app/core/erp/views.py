from django.http import HttpResponse
from django.shortcuts import render
from app.core.erp.models import Category


def first(request):
    data = {
        'name': 'michel',
        'categories': Category.objects.all()

    }

    return render(request, 'index.html', data)

def second(request):

    return HttpResponse('dosdos')
