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
from django.http import JsonResponse


from tickets.models import *


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request):
        ctx = {"brands": CarBrand.objects.all()}
        return render(request, self.template_name, ctx)
    

def get_years(request, brand_id):
    brand = CarBrand.objects.get(id=brand_id)
    years = brand.available_years
    return JsonResponse(years, safe=False)

def get_models(request, brand_id, year):
    brand = CarBrand.objects.get(id=brand_id)
    models = brand.available_models(year)
    return JsonResponse(models, safe=False)

def get_versions(request, brand_id, year, model_id):
    brand = CarBrand.objects.get(id=brand_id)
    versions = brand.available_versions(year, model_id)
    return JsonResponse(versions, safe=False)
