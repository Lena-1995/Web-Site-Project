# Generated by Django 3.0.2 on 2020-01-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0003_auto_20200120_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('book', models.FileField(upload_to='books/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='book',
            field=models.FileField(upload_to='books/'),
        ),
    ]