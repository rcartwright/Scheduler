from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from requests.models import Vacation
from requests.models import User
from requests.models import Request

def index(request):
    user_list = Vacation.objects.order_by('-days_total')[:5]
    template = loader.get_template('vacation/index.html')
    context = RequestContext(request, {
        'user_list': user_list,
    })
    return HttpResponse(template.render(context))

def edit(request, request_id):
    return HttpResponse("Edit Request" % request_id)

def show(request, request_id):
    return HttpResponse("Show Request" % request_id)

def delete(request, request_id):
    return HttpResponse("Delete Request" % request_id)