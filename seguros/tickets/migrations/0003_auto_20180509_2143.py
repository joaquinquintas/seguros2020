# Generated by Django 2.0.3 on 2018-05-09 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20180509_2142'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together=set(),
        ),
    ]