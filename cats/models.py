from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Sex(models.Model):

    class Meta:
        verbose_name_plural = 'Sexes'

    sex = models.CharField(max_length=254)

    def __str__(self):
        return self.sex

class Cat(models.Model):
    name = models.CharField(max_length=254)
    sex = models.ForeignKey('Sex', null=True, blank=True, on_delete=models.SET_NULL)
    age = models.CharField(max_length=254, help_text="Age when rescued")
    rescued = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=254, help_text="Ready to be adopted etc...")
    description = models.CharField(max_length=254, help_text="Physical Description", null=True, blank=True)
    profile = RichTextField(null=True, blank=True)
    neutered = models.BooleanField(null=True, blank=True)
    microchipped = models.BooleanField(null=True, blank=True)
    vaccinated = models.BooleanField(null=True, blank=True)
    adopted = models.BooleanField(null=True, blank=True)
    resident = models.BooleanField(null=True, blank=True)
    tagline = models.CharField(max_length=254, help_text="One line character description...", null=True, blank=True)
    health_checked = models.BooleanField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
