from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Deal, Store

# Create your views here.


def index(request):
    latest_deal_list = Deal.objects.order_by('-publish_time')[:5]
    template = loader.get_template('index.html')
    context = {'latest_deal_list': latest_deal_list}
    return HttpResponse(template.render(context, request))


def about(request):
    return HttpResponse("This is About Page")


def deal(request, deal_id):
    deal = get_object_or_404(Deal, pk=deal_id)
    template = 'deal.html'
    return render(request, template, {'deal': deal})


def details(request, deal_id):
    return HttpResponse("you are looking on Deal Number: %s " % deal_id)


def store(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    template = 'store.html'
    return render(request, template, {'store': store})
