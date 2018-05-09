# Generated by Django 2.0.3 on 2018-05-08 01:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Marca')),
                ('slug', models.SlugField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Modelo')),
                ('slug', models.SlugField(max_length=300)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='tickets.CarBrand')),
            ],
        ),
        migrations.CreateModel(
            name='CarVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infoauto_id', models.IntegerField()),
                ('name', models.CharField(max_length=150, verbose_name='Version')),
                ('slug', models.SlugField(max_length=300)),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='tickets.CarModel')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre y Apellido')),
                ('age', models.PositiveIntegerField(verbose_name='Edad')),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=100, verbose_name='Provincia')),
                ('city', models.CharField(max_length=100, verbose_name='Localidad')),
                ('phone', models.PositiveIntegerField(verbose_name='Teléfono')),
                ('car_brand', models.CharField(max_length=100, verbose_name='Marca')),
                ('car_model', models.CharField(max_length=100, verbose_name='Model')),
                ('car_version', models.CharField(max_length=100, verbose_name='Version')),
                ('car_year', models.PositiveIntegerField(choices=[(1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017')], verbose_name='Año')),
                ('status', models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Contactado'), (3, 'No contratado'), (4, 'Contratado'), (5, 'Error'), (6, 'Baja')], verbose_name='Estado')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]