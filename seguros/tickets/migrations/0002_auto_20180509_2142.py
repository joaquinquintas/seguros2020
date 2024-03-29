# Generated by Django 2.0.3 on 2018-05-09 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carbrand',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='carversion',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='carmodel',
            name='infoauto_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together={('infoauto_id', 'brand')},
        ),
    ]
