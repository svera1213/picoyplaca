from django.db import models

from ..managers import PicoyplacaConfigurationManager


class PicoyplacaConfiguration(models.Model):
    code = models.CharField(max_length=100, db_index=True)
    timezone = models.CharField(max_length=100, default='America/Guayaquil')

    start_time = models.TimeField()
    end_time = models.TimeField()

    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PicoyplacaConfigurationManager()
