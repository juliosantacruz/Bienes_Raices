# Generated by Django 3.2 on 2021-04-12 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitacional', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='images/landing', verbose_name='Imagen'),
        ),
    ]