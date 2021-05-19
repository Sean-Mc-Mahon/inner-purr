from django.db import models


class EmailContacts(models.Model):
    class Meta:
        verbose_name_plural = 'Email Contacts'
    directory = models.CharField(max_length=254)
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.directory