# Generated by Django 3.0.2 on 2020-02-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200213_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='app1\\photos', verbose_name='Foto'),
        ),
    ]
