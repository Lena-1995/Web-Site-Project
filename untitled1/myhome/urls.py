from django.conf.urls import url
from django.urls import path,include
from django.views.generic import ListView,DetailView
from myhome.models import LogUser

from . import views

urlpatterns = [
    url(r'^$', views.HOME_view, name='HOME'),

    url(r'^HOME/$', views.HOME_view, name='HOME'),

    url(r'^NEWS/$', views.NEWS_view, name='NEWS'),
    url(r'^CONTACT_US/$',views.CONTACT_US_view, name='CONTACT_US'),

    url(r'^LOGIN/DONE/$', views.LOGIN_DONE_view,name='LOGIN_DONE'),
    url(r'^REGISTER/$', views.REGISTER_view,name='REGISTER'),
    url(r'^REGISTER/DONE/$', views.REGISTER_DONE_view,name='REGISTER_DONE'),

    url(r'^WRONG/$', views.WRONG,name='WRONG'),

    url(r'^HOME/ADMIN/$', views.ADMIN_view,name='ADMIN'),
    url(r'^HOME/TEACHER/$', views.TEACHER_view,name='TEACHER'),
    url(r'^HOME/STUDENT/$', views.STUDENT_view,name='STUDENT'),

    url(r'^HOME/TEACHER/CLASS$', views.TEACHER_ADDCLASS_view,name='ADDCLASS'),

]

#Login_view
"""
    path('HOME/', DetailView.as_view(queryset=logUser,template_name="Project_site.html")),
    path('REGISTER/', DetailView.as_view(queryset=logUser,template_name="LOGIN/Register_Page.html")),
"""