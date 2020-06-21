from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage':"OMG,OMG,OMFG NE"}
    return render(request,'index.html',context = context_dict)

def about(request):
    return HttpResponse("This is About Page")

def deal(request, deal_id):
    return HttpResponse("you are looking on deals %s." % deal_id)

def details(request, deal_id):
    return HttpResponse("you are looking on Deal Number: %s " % deal_id)