# Generated by Django 2.0.3 on 2018-05-09 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20180509_2143'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together={('infoauto_id', 'brand')},
        ),
    ]
