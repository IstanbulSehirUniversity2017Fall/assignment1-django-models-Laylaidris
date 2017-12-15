# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Welcome to Money-List we are here to manage your money")

