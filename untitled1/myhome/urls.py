from django.conf.urls import url
from django.urls import path,include
from django.views.generic import ListView,DetailView
from myhome.models import LogUser

from . import views

urlpatterns = [
    url(r'^$', views.HOME_view, name='HOME'),


    url(r'^NEWS/$', views.NEWS_view, name='NEWS'),
    url(r'^CONTACT_US/$',views.CONTACT_US_view, name='CONTACT_US'),

    url(r'^ADMIN_SETTINGS/$',views.ADMIN_Settings_view, name='ADMIN_SETTINGS'),
    url(r'^ADMIN_DATA/$',views.ADMIN_Data_view, name='ADMIN_DATA'),
    url(r'^ADMIN_MESS/$',views.ADMIN_Mess_view, name='ADMIN_MESS'),
    url(r'^ADMIN_RATING/$',views.ADMIN_Rating_view, name='ADMIN_RATING'),
    url(r'^ADMIN_USERS/$',views.ADMIN_Users_view, name='ADMIN_USERS'),


    url(r'^TEACHER_SETTINGS/$',views.TEACHER_Settings_view, name='TEACHER_SETTINGS'),
    url(r'^TEACHER_DATA/$',views.TEACHER_Data_view, name='TEACHER_DATA'),
    url(r'^TEACHER_CHAT/$',views.TEACHER_Chat_view, name='TEACHER_CHAT'),
    url(r'^TEACHER_USERS/$',views.TEACHER_Users_view, name='TEACHER_USERS'),
    url(r'^TEACHER_CLASS/$',views.TEACHER_Class_view, name='TEACHER_CLASS'),
    url(r'^TEACHER_DATA/ADD_BOOK/$',views.ADD_BOOK_view, name='ADD_BOOK'),
    url(r'^TEACHER_DATA/ADD_WORD/$',views.ADD_WORD_view, name='ADD_WORD'),
    url(r'^TEACHER_CLASS/ADD_CLASS/$',views.ADD_Class_view, name='ADD_CLASS'),
    url(r'^TEACHER_USERS/ADD_USER/$',views.ADD_USER_view, name='ADD_USER'),
    url(r'^TEACHER_DATA/WORD_LIST/$',views.TEACHER_Words_view, name='WORD_LIST'),
    url(r'^TEACHER_DATA/BOOK_LIST/$',views.TEACHER_Book_view, name='BOOK_LIST'),
    url(r'^TEACHER_CLASS/ADD_TEST/$',views.ADD_TEST_view, name='ADD_TEST'),
    url(r'^TEACHER_CLASS/EST_LIST/$',views.TEST_LIST_view, name='TEST_LIST'),








    url(r'^STUDENT_ALPHABET/$',views.STUDENT_Alphabet_view, name='STUDENT_ALPHABET'),
    url(r'^STUDENT_BOOKS/$',views.STUDENT_Books_view, name='STUDENT_BOOKS'),
    url(r'^STUDENT_WORDS/$',views.STUDENT_Words_view, name='STUDENT_WORDS'),
    url(r'^STUDENT_TEST/$',views.STUDENT_Test_view, name='STUDENT_TEST'),
    url(r'^STUDENT_TEST/logout$', views.logout_request, name="logout"),
    url(r'^STUDENT_WORDS/logout$', views.logout_request, name="logout"),
    url(r'^STUDENT_BOOKS/logout$', views.logout_request, name="logout"),
    url(r'^STUDENT_ALPHABET/logout$', views.logout_request, name="logout"),


    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),

]

#Login_view
"""
    path('HOME/', DetailView.as_view(queryset=logUser,template_name="Project_site.html")),
    path('REGISTER/', DetailView.as_view(queryset=logUser,template_name="LOGIN/Register_Page.html")),
"""

"""




path("register/", views.register, name="register"),
path("logout", views.logout_request, name="logout"),
path("login", views.login_request, name="login"),
"""