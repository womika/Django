from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# Create your views here.


# def index(request):
#     return HttpResponse("Hello, world. You're at the doctors index.")

def index(request):
    return render(request, 'add_many.html', {'table_name': 'cos',
                                             'form': 'aform'})
