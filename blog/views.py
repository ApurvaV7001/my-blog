from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

# Create your views here.

def func(request):
    object=Post.objects.all()
    return render(request,'base.html',{'object':object,})