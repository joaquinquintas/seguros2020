from django.db import models
from model_utils.models import TimeStampedModel


class Tickets(TimeStampedModel):

    STATUS = (
        (1, 'Pendiente'),
        (2, 'Contactado'),
        (3, 'No contratado'),
        (4, 'Contratado'),
        (5, 'Error'),
        (6, 'Baja'),
    )

    name = models.CharField(verbose_name='Nombre y Apellido', max_length=150)
    age = models.PositiveIntegerField(verbose_name='Edad')
    email = models.EmailField()
    state = models.CharField(verbose_name='Provincia', max_length=100)
    city = models.CharField(verbose_name='Localidad', max_length=100)
    phone = models.PositiveIntegerField(verbose_name='Teléfono')
    car_brand = models.CharField(verbose_name='Marca', max_length=100)
    car_model = models.CharField(verbose_name='Model', max_length=100)
    car_version = models.CharField(verbose_name='Version', max_length=100)
    car_year = models.PositiveIntegerField(verbose_name='Año',
                                           choices=[(y, str(y)) for y in range(1998, 2018)]
                                           )
    status = models.IntegerField(verbose_name='Estado', choices=STATUS)

class CarBrand(models.Model):
    name = models.CharField(verbose_name='Marca', max_length=150)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

    
    @property
    def available_years(self):
        return list(CarVersion.objects.filter(brand=self).order_by("-year").distinct().values_list('year',flat=True))
    
    def available_models(self, year):
        return list(CarVersion.objects.filter(brand=self, 
                                              year=year).order_by("model__name")\
                    .distinct().values(
                                'model__id',
                                'model__infoauto_id',
                                'model__name'))
        
    def available_versions(self, year, model_id):
        return list(CarVersion.objects.filter(brand=self, 
                                              year=year,
                                              model__id=model_id).order_by("name")\
                    .distinct().values(
                                'id',
                                'name',
                                'infoauto_id',
                                'year',
                                'price'))
    
class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, related_name="models", on_delete=models.CASCADE)
    infoauto_id = models.IntegerField()
    name = models.CharField(verbose_name='Modelo', max_length=150)
    slug = models.SlugField(max_length=300)
    
    @property
    def brand_name(self):
        return self.brand.name
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        unique_together = (("infoauto_id", "brand"),)
        

class CarVersion(models.Model):
    infoauto_id = models.IntegerField()
    brand = models.ForeignKey(CarBrand, related_name="brand_versions", on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, related_name="versions", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Version', max_length=150)
    slug = models.SlugField(max_length=300)
    year = models.IntegerField()
    price = models.IntegerField()
    
    class Meta:
        ordering = ["name"]
    
    @property
    def brand_name(self):
        return self.model.brand.name
    
    @property
    def model_name(self):
        return self.model.name
      
    