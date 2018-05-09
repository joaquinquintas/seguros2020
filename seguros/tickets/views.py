# coding=utf-8

from __future__ import unicode_literals


from django.views.generic.base import TemplateView
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404


from tickets.models import *


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request):
        ctx = {"brands": CarBrand.objects.all()}
        return render(request, self.template_name, ctx)
    
    