from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse
def insert_Topic(request):
    t0=input('enter topic name')
    t1=Topic.objects.get_or_create(Topic_name=t0)[0]
    t1.save()
    return HttpResponse('data is inserted')

def insert_Webpage(request):
    t0=input('enter topic name')
    t1=Topic.objects.get_or_create(Topic_name=t0)[0]
    t1.save()
    
    n=input('enter name')
    u=input('enter url')
    t2=Webpage.objects.get_or_create(Topic_name=t1,Name=n,url=u)[0]
    t2.save()
    return HttpResponse('webpage data is inserted')
def insert_AccessRecords(request):
    t0=input('enter topic name')
    t1=Topic.objects.get_or_create(Topic_name=t0)[0]
    t1.save()
    
    n=input('enter name')
    u=input('enter url')
    t2=Webpage.objects.get_or_create(Topic_name=t1,Name=n,url=u)[0]
    t2.save()
    d=input('enter date')
    a=input('enter author name')


    t3=AccessRecords.objects.get_or_create(Name=t2,date=d,author=a)[0]
    t3.save()
    return HttpResponse('access records data is inserted')

