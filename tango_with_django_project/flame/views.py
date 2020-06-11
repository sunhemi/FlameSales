from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage':"OMG,OMG,OMFG NE"}
    return render(request,'index.html',context = context_dict)

def about(request):
    return HttpResponse("This is About Page")

def deals(request, question_id):
    return HttpResponse("you are looking on deals %s." % question_id)

