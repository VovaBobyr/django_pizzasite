# Generated by Django 3.0.3 on 2020-02-13 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200213_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'ordering': ['name'], 'verbose_name': 'Pizzeria', 'verbose_name_plural': 'Pizzas'},
        ),
    ]
