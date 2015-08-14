from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    admin = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.id)

class Request(models.Model):
    user = models.ForeignKey(User)
    request_text = models.CharField(max_length=200)
    request_date = models.DateTimeField('date requested')
    days = models.IntegerField()
    approved = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.request_text

class Vacation(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    days = models.CharField(max_length=200)
    days_total = models.IntegerField()

