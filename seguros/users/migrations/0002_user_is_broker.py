# Generated by Django 2.0.3 on 2018-03-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_broker',
            field=models.BooleanField(default=False),
        ),
    ]
