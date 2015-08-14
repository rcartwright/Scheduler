from django.shortcuts import render

from django.http import HttpResponse

from requests.models import Vacation

def index(request):
    user_list = Vacation.objects.order_by('-days_total')[:5]
    output = ', '.join([str(i) for i in user_list])
    return HttpResponse(output)

def edit(request, request_id):
    return HttpResponse("Edit Request" % request_id)

def show(request, request_id):
    return HttpResponse("Show Request" % request_id)

def delete(request, request_id):
    return HttpResponse("Delete Request" % request_id)