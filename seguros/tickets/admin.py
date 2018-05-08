# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from tickets.models import CarBrand, CarModel, CarVersion

admin.site.site_header = 'Seguros2020 Admin'


class CarBrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)


class CarModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('brand_name', 'name',)

class CarVersionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('brand_name', 'model_name', 'name', 'year', 'price')
    list_filter = ('model__brand', 'year')
    
admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarVersion, CarVersionAdmin)
