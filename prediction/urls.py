# prediction/urls.py
from django.urls import path # type: ignore
from .views import predict_diabetes

urlpatterns = [
    path('', predict_diabetes, name='predict_diabetes'),
]
