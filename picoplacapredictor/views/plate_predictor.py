from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import PlatePredictorService


class PlatePredictor(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request, plate):
        search_date = self.request.GET.get('search_date')
        search_time = self.request.GET.get('search_time')

        svc = PlatePredictorService(plate, search_date, search_time)
        is_allowed = svc.is_plate_allowed()
        return Response(data={'is_allowed': is_allowed}, status=status.HTTP_200_OK)
