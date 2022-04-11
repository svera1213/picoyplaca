from datetime import date, time, datetime
from re import match
from pytz import timezone as pytz_timezone

from ..models import PicoyplacaConfiguration, PicoyplacaDay, PicoyplacaPause

FORMAT_DATETIME = '%Y-%m-%d %H:%M:%S'


class PlatePredictorService:
    def __init__(self, plate: str, date: str = '', time: str = ''):
        self.plate = plate
        self.date = date
        self.time = time

    def is_plate_allowed(self):
        if self.date and self.time:
            datetime_str = f'{self.date} {self.time}'
            search_datetime = datetime.strptime(datetime_str, FORMAT_DATETIME)
        else:
            search_datetime = datetime.now()

        search_date = search_datetime.date()
        search_time = search_datetime.time()

        config = PicoyplacaConfiguration.objects.find_current_configuration()
        if config and config.timezone:
            new_timezone = pytz_timezone(config.timezone)
            search_datetime = search_datetime.astimezone(new_timezone)
            search_date = search_datetime.date()
            search_time = search_datetime.time()

        iso_weekday = search_date.isoweekday()

        in_pause = PicoyplacaPause.objects.is_in_pause(config.id, search_time)
        if in_pause:
            return True

        day_restriction = PicoyplacaDay.objects.find_day_restriction(config.id, iso_weekday)

        if not day_restriction:
            return True

        print(day_restriction.plate_key)

        match_regex = match(day_restriction.plate_key, self.plate)

        print(match_regex)
        if match_regex:
            return False

        return True
