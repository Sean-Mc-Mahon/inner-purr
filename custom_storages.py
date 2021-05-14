from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

#  code taken from CI module @ https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/2229819dd50d944117bfe9837c590d59d70bbc66/custom_storages.py