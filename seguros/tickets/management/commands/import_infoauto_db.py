# coding=utf-8

""" Command to test the game modified functionality sending async notifications """

from __future__ import unicode_literals


import csv
import environ

from django.utils.text import slugify
from django.core.management.base import BaseCommand


from tickets.models import CarBrand, CarModel, CarVersion


ROOT_DIR = environ.Path(__file__) - 4

class Command(BaseCommand):

    def handle(self, *args, **options):
        #self.import_brands()
        #self.import_models()
        self.import_versions()
    
    def import_brands(self):
        AUTOS_DIR = ROOT_DIR.path('infoauto_db/tautos.csv')

        with open(str(AUTOS_DIR)) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)
                brand, _ = CarBrand.objects.get_or_create(id=row[0])
                brand.name = row[1]
                brand.slug = slugify(row[1])
                brand.save()
    
    def import_models(self):
        GRUPOS_DIR = ROOT_DIR.path('infoauto_db/grupos.csv')

        with open(str(GRUPOS_DIR)) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)
                try:
                    brand = CarBrand.objects.get(id=row[0])
                except CarBrand.DoesNotExist:
                    print ("Does not exist: %s"%row[0])
                    continue
                    
                try:
                    
                    model = CarModel.objects.get(infoauto_id=row[1], brand=brand)
                    model.name = row[2]
                    model.slug = slugify(row[2])
                    model.save()
                    
                except CarModel.DoesNotExist:
                    model = CarModel.objects.create(infoauto_id=row[1], brand=brand, name = row[2], slug = slugify(row[2]))
                    
    
    def import_versions(self):
        AUTOS_DIR = ROOT_DIR.path('infoauto_db/tautos.csv')

        with open(str(AUTOS_DIR)) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)
                brand = CarBrand.objects.get(id=row[0])
                model = CarModel.objects.get(id=row[5])
                
                infoauto_id = row[4]
                name = row[3]
                slug = slugify(name)
                
                price_2018 = int(row[8])
                if price_2018 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2018)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2018,
                                                  brand=brand,
                                                  price=price_2018* 1000)
                
                price_2017 = int(row[9])
                if price_2017 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2017)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2017,
                                                  brand=brand,
                                                  price=price_2017* 1000)
                
                price_2016 = int(row[10])
                if price_2016 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2016)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2016,
                                                  brand=brand,
                                                  price=price_2016* 1000)
                
                price_2015 = int(row[11])
                if price_2015 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2015)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2015,
                                                  brand=brand,
                                                  price=price_2015* 1000)
                price_2014 = int(row[12])
                if price_2014 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2014)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2014,
                                                  brand=brand,
                                                  price=price_2014* 1000)
                
                price_2013 = int(row[13])
                if price_2013 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2013)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2013,
                                                  brand=brand,
                                                  price=price_2013* 1000)
                        
                price_2012 = int(row[14])
                if price_2012 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2012)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2012,
                                                  brand=brand,
                                                  price=price_2012* 1000)
                        
                price_2011 = int(row[15])
                if price_2011 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2011)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2011,
                                                  brand=brand,
                                                  price=price_2011* 1000)
                
                price_2010 = int(row[16])
                if price_2010 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2010)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2010,
                                                  brand=brand,
                                                  price=price_2010* 1000)
                        
                price_2009 = int(row[17])
                if price_2009 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2009)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2009,
                                                  brand=brand,
                                                  price=price_2009* 1000)
                        
                price_2008 = int(row[17])
                if price_2008 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2008)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2008,
                                                  brand=brand,
                                                  price=price_2008 * 1000)
                 
                price_2007 = int(row[18])
                if price_2007 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2007)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2007,
                                                  brand=brand,
                                                  price=price_2007 * 1000)
                price_2006 = int(row[19])
                if price_2006 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2006)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2006,
                                                  brand=brand,
                                                  price=price_2006 * 1000) 
                price_2005 = int(row[20])
                if price_2005 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2005)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2005,
                                                  brand=brand,
                                                  price=price_2005 * 1000) 
                
                
                price_2004 = int(row[21])
                if price_2004 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2004)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2004,
                                                  brand=brand,
                                                  price=price_2004 * 1000) 
                        
                price_2003 = int(row[22])
                if price_2003 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2003)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2003,
                                                  brand=brand,
                                                  price=price_2003 * 1000)
                
                price_2002 = int(row[23])
                if price_2002 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2002)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2002,
                                                  brand=brand,
                                                  price=price_2002 * 1000)
                        
                price_2001 = int(row[24])
                if price_2001 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2001)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2001,
                                                  brand=brand,
                                                  price=price_2001 * 1000)
                        
                price_2000 = int(row[25])
                if price_2000 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=2000)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=2000,
                                                  brand=brand,
                                                  price=price_2000 * 1000)
                
                price_1999 = int(row[26])
                if price_1999 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=1999)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=1999,
                                                  brand=brand,
                                                  price=price_1999 * 1000)
                
                price_1998 = int(row[27])
                if price_1998 != 0:
                    try:
                        CarVersion.objects.get(slug=slug, year=1998)
                    except CarVersion.DoesNotExist:
                        CarVersion.objects.create(infoauto_id=infoauto_id, 
                                                  name=name, slug=slug,
                                                  model=model,
                                                  year=1998,
                                                  brand=brand,
                                                  price=price_1998 * 1000)
                        