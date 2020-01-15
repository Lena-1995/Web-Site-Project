from django.urls import path
from . import views



urlpatterns = [
    path('', views.HOME_view, name='home-page'),
    path('LOGIN/LOGED/', views.LOGED_view),
    path('LOGIN/REGISTER/', views.REGISTER_view),
    path('LOGIN/REGISTER/SUCCESS/', views.success_view),
    path('USERS/ADMIN/', views.ADMIN_view),
    path('USERS/ADMIN/SETTINGS/', views.ADMIN_SETTINGS_view),
    path('USERS/ADMIN/USERS/', views.ADMIN_USERS_view),
    path('USERS/ADMIN/USERS/TEACHERS/CLASS/', views.ADMIN_USERS_TEACHERS_CLASS_view),
    path('USERS/ADMIN/USERS/TEACHERS/CLASS/STUDENTS/', views.ADMIN_USERS_TEACHERS_CLASS_STUDENTS_view),
    path('USERS/STUDENT/', views.STUDENT_view),
    path('USERS/STUDENT/ALPHABET/', views.STUDENT_ALPHABET_view),
    path('USERS/STUDENT/BOOKS/', views.STUDENT_BOOKS_view),
    path('USERS/STUDENT/TEST/', views.STUDENT_TEST_view),
    path('USERS/STUDENT/WORDS/', views.STUDENT_WORDS_view),
    path('USERS/TEACHER/', views.TEACHER_view),






]
