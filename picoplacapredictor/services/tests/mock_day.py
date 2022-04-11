from unittest import mock

from django.db.models import QuerySet

from ...models.picoyplaca_day import PicoyplacaDayManager, PicoyplacaDay


class MockPicoyplacaDayManager(PicoyplacaDayManager):
    mock_query_set = mock.Mock(spec=QuerySet)

    def find_day_restriction(self, base_configuration_id, day):
        return PicoyplacaDay(plate_key='^.+?[9,0]$')

