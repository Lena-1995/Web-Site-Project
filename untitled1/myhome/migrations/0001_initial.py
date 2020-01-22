# Generated by Django 3.0.2 on 2020-01-17 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('book', models.FileField(upload_to='media/books/')),
            ],
        ),
        migrations.CreateModel(
            name='LogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sitesetiings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudentTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('q1', models.TextField(max_length=128)),
                ('q2', models.TextField(max_length=128)),
                ('q3', models.TextField(max_length=128)),
                ('q4', models.TextField(max_length=128)),
                ('q5', models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TEST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('img', models.ImageField(upload_to='media/words/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sitesetiings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myhome.Sitesetiings')),
                ('name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('classname', models.CharField(max_length=128)),
            ],
            bases=('myhome.sitesetiings',),
        ),
    ]
