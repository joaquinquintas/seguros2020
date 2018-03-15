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
                                           choices=[(y, str(y)) for y in range(1880, 2018)]
                                           )
    status = models.IntegerField(verbose_name='Estado', choices=STATUS)

