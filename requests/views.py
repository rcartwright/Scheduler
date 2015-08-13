from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Request Index")

def edit(request, request_id):
    return HttpResponse("Edit Request" % request_id)

def show(request, request_id):
    return HttpResponse("Show Request" % request_id)

def delete(request, request_id):
    return HttpResponse("Delete Request" % request_id)