# Generated by Django 3.0.3 on 2020-02-13 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name of pizza')),
                ('sort_description', models.CharField(max_length=30, verbose_name='Short description')),
                ('price', models.IntegerField(default=0, verbose_name='Price of pizza')),
                ('pizzashopFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.pizzaShop')),
            ],
        ),
    ]
