from django.urls import path, include

from .views import PlatePredictor

app_name = 'picoyplacapredictor_api'

urlpatterns = [
    path('predictor/plates/<str:plate>', name='plates_predictor', view=PlatePredictor.as_view())
]
