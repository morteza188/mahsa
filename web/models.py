# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=512)
    def __unicode__(self):
        return "{}_token".format(self.user)

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.text + "    {}".format(self.amount)

class InCome(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.text + "    {}".format(self.amount)

class Note(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.text + "    {}".format(self.text)

class Task(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    #deadline = models.DateTimeField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.text + "    {}".format(self.text)
