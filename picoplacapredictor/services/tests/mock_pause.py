from unittest import mock

from django.db.models import QuerySet

from ...models.picoyplaca_pause import PicoyplacaPauseManager


class MockPicoyplacaPauseManager(PicoyplacaPauseManager):
    mock_query_set = mock.Mock(spec=QuerySet)

    def is_in_pause(self, base_configuration_id, search_time):
        return False
