from unittest import mock

from django.db.models import QuerySet

from ...managers import PicoyplacaConfigurationManager
from ...models import PicoyplacaConfiguration


class MockPicoyplacaConfigurationManager(PicoyplacaConfigurationManager):
    mock_query_set = mock.Mock(spec=QuerySet)

    def find_current_configuration(self):
        return PicoyplacaConfiguration(id=1)

