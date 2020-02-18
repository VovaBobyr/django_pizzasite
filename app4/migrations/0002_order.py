# Generated by Django 3.0.2 on 2020-02-18 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.Pizza')),
            ],
        ),
    ]
