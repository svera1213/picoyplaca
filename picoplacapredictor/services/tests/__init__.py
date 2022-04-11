from unittest import mock

from django.test import SimpleTestCase

from .mock_configuration import MockPicoyplacaConfigurationManager
from .mock_day import MockPicoyplacaDayManager
from .mock_pause import MockPicoyplacaPauseManager
from ...models import PicoyplacaConfiguration, PicoyplacaPause, PicoyplacaDay
from ...services import PlatePredictorService


class PlatePredictorServiceTest(SimpleTestCase):

    def setUp(self):
        PicoyplacaConfiguration.objects = MockPicoyplacaConfigurationManager()
        PicoyplacaDay.objects = MockPicoyplacaDayManager()
        PicoyplacaPause.objects = MockPicoyplacaPauseManager()

    def test_plate_on_valid_day(self):
        svc = PlatePredictorService("PHP-222", "2022-04-11", "11:30:00")
        allowed = svc.is_plate_allowed()
        self.assertEqual(True, allowed)

    def test_plate_on_restricted_day(self):
        svc = PlatePredictorService("PHP-229", "2022-04-11", "11:30:00")
        allowed = svc.is_plate_allowed()
        self.assertEqual(False, allowed)

