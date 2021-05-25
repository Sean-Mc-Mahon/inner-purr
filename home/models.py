from django.db import models
from ckeditor.fields import RichTextField


class Drink(models.Model):
    class Meta:
        verbose_name_plural = 'Drinks'
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    class Meta:
        verbose_name_plural = 'Food'
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=254, null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Treats(models.Model):
    class Meta:
        verbose_name_plural = 'Treats'
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=254, null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name
        
class Notice(models.Model):
    notice = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.notice