from django.db import models


class Event(models.Model):
    session_id = models.UUIDField()
    category = models.CharField()
    name = models.CharField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['timestamp']


class PageView(models.Model):
    event = models.ForeignKey('the_eye.Event', on_delete=models.CASCADE)
    host = models.CharField()
    path = models.CharField()


class PageClick(models.Model):
    event = models.ForeignKey('the_eye.Event', on_delete=models.CASCADE)
    host = models.CharField()
    path = models.CharField()
    element = models.CharField()


class AccountSubmit(models.Model):
    event = models.ForeignKey('the_eye.Event', on_delete=models.CASCADE)
    host = models.CharField()
    path = models.CharField()


class Account(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    account_submit = models.ForeignKey('the_eye.AccountSubmit', on_delete=models.CASCADE)
