# Generated by Django 3.2.6 on 2021-09-21 14:25

from django.db import migrations, models
from django.db.models.fields import PositiveIntegerField

class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('dni', models.PositiveIntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('born_date', models.DateTimeField(verbose_name='date birth')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
