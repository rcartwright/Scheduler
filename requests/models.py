from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)



class Request(models.Model):
    user = models.ForeignKey(User)
    request_text = models.CharField(max_length=200)
    request_date = models.DateTimeField('date requested')