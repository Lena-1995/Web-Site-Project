# Generated by Django 3.0.2 on 2020-01-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
