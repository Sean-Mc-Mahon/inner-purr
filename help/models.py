from django.db import models
from ckeditor.fields import RichTextField


class Volunteer(models.Model):
    class Meta:
        verbose_name_plural = 'Volunteering'
    role = models.CharField(max_length=254)
    description = RichTextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.role


class Donations(models.Model):
    class Meta:
        verbose_name_plural = 'Donations'
    donation_option = models.CharField(max_length=254)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.donation_option


class Notice(models.Model):
    notice = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.notice
