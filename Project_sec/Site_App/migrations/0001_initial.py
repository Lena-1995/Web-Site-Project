# Generated by Django 3.0 on 2019-12-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=64)),
                ('UserPass', models.CharField(max_length=64)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]