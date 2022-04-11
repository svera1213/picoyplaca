from datetime import time
from django.db import models


class PicoyplacaConfigurationManager(models.Manager):

    def find_current_configuration(self):
        config = self.get_queryset().filter(enabled=True).last()
        return config
