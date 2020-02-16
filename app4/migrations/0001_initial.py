# Generated by Django 3.0.2 on 2020-02-15 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pizzaShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Pizzeria')),
                ('description', models.TextField(verbose_name='Description')),
                ('raiting', models.FloatField(default=0, verbose_name='Raiting')),
                ('url', models.URLField(verbose_name='Internet address')),
            ],
            options={
                'verbose_name': 'Pizzeria',
                'verbose_name_plural': 'Pizzerias',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name of pizza')),
                ('sort_description', models.CharField(max_length=30, verbose_name='Short description')),
                ('price', models.IntegerField(default=0, verbose_name='Price of pizza')),
                ('photo', models.ImageField(blank=True, default='', upload_to='app1\\photos', verbose_name='Foto')),
                ('pizzashopFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.pizzaShop')),
            ],
            options={
                'verbose_name': 'Pizzeria',
                'verbose_name_plural': 'Pizzas',
                'ordering': ['name'],
            },
        ),
    ]