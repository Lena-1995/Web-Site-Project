from django.urls import path
from . import views



urlpatterns = [
    path('', views.TEST_FUN, name='home-page'),
]
