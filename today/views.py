from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.
def All(request):
    all=Post.objects.filter(title='django')
    context={'all':all,
             'title':'feras'}
    return render(request,'today/all.html',context)
def Feras(request):
    return render(request,'today/feras.html')