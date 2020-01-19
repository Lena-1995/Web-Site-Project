from django.shortcuts import render
from django.http import HttpResponse
from .models import LogUser
# Create your views here.




def HOME_view(request):
    if request.method == 'POST':
        test_name=request.POST.get('uname')
        test_psw = request.POST.get('psw')
        if str(test_name) is "ADMIN" and str(test_psw) is "ADMIN":
            logUser=LogUser()

            logUser.login("ADMIN","ADMIN")
        #elif test_name in teacher.objects.

    return render(
        request,
        'Project_site.html',{}
        #peredacha danih v html

    )


def WRONG(request):
    return render(request,'LOGIN/WRONG.html')

def HOME(request):

    return render(
        request,
        'Project_site.html',


    )

def LOGIN_DONE_view(request):
    return render(
        request,
        'LOGIN/LOGED AS.html',
    )

def REGISTER_view(request):

    return render(

        request,
        'LOGIN/Register_Page.html',{'LogUser':logUser.getuser(),'LogUserr':logUser.getuser()

        }
    )

def REGISTER_DONE_view(request):
    return render(
        request,
        'LOGIN/SECSES.html',
    )




def NEWS_view(request):
    return render(
        request,
        'News.html',
    )

def CONTACT_US_view(request):
    return render(
        request,
        'CONTACT_US.html',
    )

def ADMIN_view(request):
    return render(
        request,
        'USERS/ADMIN/ADMIN_page.html',
    )

def TEACHER_view(request):
    return render(
        request,
        'USERS/TEACHER/Teacher_page.html',
    )

def STUDENT_view(request):
    return render(
        request,
        'USERS/STUDENT/Student_page.html',
    )

def TEACHER_ADDCLASS_view(request):
    return render(
        request,
        'USERS/TEACHER/CLASS/STUDENT_REGISTRATION/Student_Register_Page.html',
    )