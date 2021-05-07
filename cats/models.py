from django.db import models


class Status(models.Model):

    class Meta:
        verbose_name_plural = 'Status'

    status = models.CharField(max_length=254)

    def __str__(self):
        return self.status

class Sex(models.Model):

    class Meta:
        verbose_name_plural = 'Sexes'

    sex = models.CharField(max_length=254)

    def __str__(self):
        return self.sex

class Cat(models.Model):
    status = models.ForeignKey('Status', null=True, blank=True, on_delete=models.SET_NULL)
    sex = models.ForeignKey('Sex', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
