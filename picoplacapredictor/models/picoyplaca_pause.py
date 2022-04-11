from datetime import time

from django.db import models


class PicoyplacaPauseManager(models.Manager):

    def is_in_pause(self, base_configuration_id: int, search_time: time):
        in_pause = self.get_queryset().filter(
            base_configuration_id=base_configuration_id, start_time__lte=search_time, end_time__gte=search_time
        ).exists()
        return in_pause


class PicoyplacaPause(models.Model):
    base_configuration = models.ForeignKey('PicoyplacaConfiguration', on_delete=models.CASCADE,
                                           related_name='configured_pauses')

    start_time = models.TimeField()
    end_time = models.TimeField()

    objects = PicoyplacaPauseManager()
