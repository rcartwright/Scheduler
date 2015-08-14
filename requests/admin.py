from django.contrib import admin

from requests.models import Request

from requests.models import User


class Request_id_display(admin.ModelAdmin):
    list_display = ['id', 'request_text', 'request_date',] 

class User_id_display(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',] 

admin.site.register(User, User_id_display)
admin.site.register(Request, Request_id_display,)
