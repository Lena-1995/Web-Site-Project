# Generated by Django 3.0.2 on 2020-01-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0002_auto_20200120_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='words',
            name='img',
            field=models.ImageField(upload_to='media/words/'),
        ),
    ]