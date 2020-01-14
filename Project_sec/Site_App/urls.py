from django.urls import path
from . import views



urlpatterns = [
    path('', views.HOME_view, name='home-page'),
    path('LOGIN/REGISTER/', views.REGISTER_view),
    path('USERS/ADMIN/', views.ADMIN_view),
]
