from datetime import date, time, datetime
from pytz import timezone as pytz_timezone

from django.core.management.base import BaseCommand, CommandError

from picoplacapredictor.models import PicoyplacaConfiguration, PicoyplacaDay, PicoyplacaPause

ec_timezone = pytz_timezone("America/Guayaquil")
BASE_CONFIG = {
    "code": "Default",
    "timezone": "America/Guayaquil",
    "start_time": datetime.now().replace(hour=6, minute=0, second=0).astimezone(ec_timezone).time(),
    "end_time": datetime.now().replace(hour=21, minute=0, second=0).astimezone(ec_timezone).time(),
}

DAYS = [
    {
        "day": 1,
        "plate_key": "^.+?[1,2]$",
    },
    {
        "day": 2,
        "plate_key": "^.+?[3,4]$",
    },
    {
        "day": 3,
        "plate_key": "^.+?[5,6]$",
    },
    {
        "day": 4,
        "plate_key": "^.+?[7,8]$",
    },
    {
        "day": 5,
        "plate_key": "^.+?[9,0]$",
    },
]

PAUSE_CONFIG = {
    "start_time": datetime.now().replace(hour=9, minute=30, second=0).astimezone(ec_timezone).time(),
    "end_time": datetime.now().replace(hour=16, minute=0, second=0).astimezone(ec_timezone).time(),
}


class Command(BaseCommand):
    help = 'Generates test data'

    def handle(self, *args, **options):
        config = PicoyplacaConfiguration.objects.create(
            code=BASE_CONFIG['code'],
            timezone=BASE_CONFIG['timezone'],
            start_time=BASE_CONFIG['start_time'],
            end_time=BASE_CONFIG['end_time'],
        )

        day_configs = []
        for day in DAYS:
            day_config = PicoyplacaDay(
                base_configuration_id=config.id,
                day=day['day'],
                plate_key=day['plate_key'],
            )
            day_configs.append(day_config)

        PicoyplacaDay.objects.bulk_create(day_configs)

        PicoyplacaPause.objects.create(
            base_configuration_id=config.id,
            start_time=PAUSE_CONFIG['start_time'],
            end_time=PAUSE_CONFIG['end_time'],
        )
