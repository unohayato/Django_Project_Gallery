from django.urls import path
from . import views

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
]
