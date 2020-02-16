from django.db import models

# Create your models here.

class pizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Pizzeria')
    description = models.TextField(verbose_name='Description')
    raiting = models.FloatField(default=0, verbose_name='Raiting')
    url = models.URLField(verbose_name='Internet address')

    class Meta:
        verbose_name='Pizzeria'
        verbose_name_plural='Pizzerias'

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashopFK = models.ForeignKey(pizzaShop, on_delete=models.CASCADE)
    #pizzashopFK2= models.ManyToManyField
    #pizzashopFK3 = models.OneToOneField
    name = models.CharField(max_length=30, verbose_name='Name of pizza')
    sort_description = models.CharField(max_length=30, verbose_name='Short description')
    price = models.IntegerField(default=0, verbose_name='Price of pizza')
    photo = models.ImageField('Foto', upload_to='app1\photos', default='', blank=True)

    class Meta:
        verbose_name='Pizzeria'
        verbose_name_plural='Pizzas'
        ordering=['name']

    def __str__(self):
        return self.name
