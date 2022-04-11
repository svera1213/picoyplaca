from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class PicoyplacaDayManager(models.Manager):

    def find_day_restriction(self, base_configuration_id: int, day: int):
        day_restriction = self.get_queryset().filter(base_configuration=base_configuration_id, day=day).last()
        return day_restriction

    
class PicoyplacaDay(models.Model):
    base_configuration = models.ForeignKey('PicoyplacaConfiguration', on_delete=models.CASCADE,
                                           related_name='configured_days')

    day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], help_text="ISO week day")
    plate_key = models.CharField(max_length=100)

    objects = PicoyplacaDayManager()
