from django.db import models


class Event(models.Model):
    session_id = models.UUIDField()
    category = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['timestamp']


class PageView(models.Model):
    event = models.ForeignKey('the_eye.Event', on_delete=models.CASCADE)
    host = models.CharField(max_length=150)
    path = models.CharField(max_length=250)


class PageClick(models.Model):
    event = models.ForeignKey('the_eye.Event', on_delete=models.CASCADE)
    host = models.CharField(max_length=150)
    path = models.CharField(max_length=250)
    element = models.CharField(max_length=150)


class EventForm(models.Model):
    event = models.ForeignKey('the_eye.Event', on_delete=models.CASCADE)
    host = models.CharField(max_length=150)
    path = models.CharField(max_length=250)


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    event_form = models.ForeignKey('the_eye.EventForm', on_delete=models.CASCADE)
