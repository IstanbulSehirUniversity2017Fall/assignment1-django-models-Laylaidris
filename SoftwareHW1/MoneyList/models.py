# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MoneyList(models.Model):
    From = models.CharField(max_length=200)
    To = models.CharField(max_length=200)
    def __str__(self):
        return "From: " + self.From + " To " + self.To

class MoneyListAmount(models.Model):
    Amount_of_money = models.ForeignKey(MoneyList, on_delete = models.CASCADE)
    def __str__(self):
        return " The Amount of Money is: " + str(self.Amount_of_money)
