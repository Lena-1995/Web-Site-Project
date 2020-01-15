from django.shortcuts import render
from .forms import SingInForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.

def HOME_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'Project_site.html')
    # return HttpResponse('<h1>This is my home page</h1>')


def LOGED_view(request):


    return render(request, 'LOGIN/LOGED AS.html')



def REGISTER_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'LOGIN/REGISTER/Register_Page.html')






def success_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'LOGIN/REGISTER/REGISTER SECCSES/SECSES.html')



def ADMIN_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/ADMIN_page.html')




def ADMIN_SETTINGS_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/SETTINGS/SETTINGS.html')








def ADMIN_USERS_view(request):

    return render(request, 'USERS/ADMIN/USERS/USERS.html')







def ADMIN_USERS_TEACHERS_CLASS_view(request):

    return render(request, 'USERS/ADMIN/USERS/TEACHERS/CLASS.html')

def ADMIN_USERS_TEACHERS_CLASS_STUDENTS_view(request):

    return render(request, 'USERS/ADMIN/USERS/TEACHERS/CLASS/STUDENTS.html')



def STUDENT_view(request):

    return render(request, 'USERS/STUDENT/Student_page.html')

def STUDENT_ALPHABET_view(request):

    return render(request, 'USERS/STUDENT/ALPHABET/ALPHABET.html')


def STUDENT_BOOKS_view(request):

    return render(request, 'USERS/STUDENT/BOOKS/BOOKS.html')


def STUDENT_TEST_view(request):

    return render(request, 'USERS/STUDENT/TEST/TEST.html')

def STUDENT_WORDS_view(request):

    return render(request, 'USERS/STUDENT/WORDS/WORDS.html')




def TEACHER_view(request):

    return render(request, 'USERS/TEACHER/Teacher_page.html')












'''

def contact(request):
    return render(request, 'TEST_APP/SITE_TEST_2.html' , {'content':['content ','content']}) #dictionaries

'''

'''
from django.shortcuts import render
from .forms import SingInForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.

def HOME_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'Project_site.html')
    # return HttpResponse('<h1>This is my home page</h1>')


def LOGED_view(request):


    return render(request, 'LOGIN/LOGED AS.html')



def REGISTER_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'LOGIN/REGISTER/Register_Page.html')






def success_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'LOGIN/REGISTER/REGISTER SECCSES/SECSES.html')



def ADMIN_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/ADMIN_page.html')


def ADMIN_DATA_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/DATA/')



def ADMIN_DATA_BASE_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/DATABASE/')



def ADMIN_DATA_BASE_BOOKS_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/DATABASE/BOOKS')



def ADMIN_DATA_BASE_PIC_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/DATABASE/PIC/')


def ADMIN_DATA_BASE_WORDS_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/DATABASE/WORDS/')


def ADMIN_RETING_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/RETING/')



def ADMIN_SETTINGS_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/SETTINGS/SETTINGS.html')


def ADMIN_SETTINGS_DISPLAY_view(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'USERS/ADMIN/SETTINGS/DISPLAY/')


def ADMIN_SETTINGS__SITE_SETTINGS_view(request):

    return render(request, 'USERS/ADMIN/SETTINGS/SITE SETTINGS/')







def ADMIN_USERS_view(request):

    return render(request, 'USERS/ADMIN/USERS/USERS.html')





def ADMIN_USERS_TEACHERS_view(request):

    return render(request, 'USERS/ADMIN/USERS/TEACHERS/')



def ADMIN_USERS_TEACHERS_CLASS_view(request):

    return render(request, 'USERS/ADMIN/USERS/TEACHERS/CLASS.html')

def ADMIN_USERS_TEACHERS_CLASS_STUDENTS_view(request):

    return render(request, 'USERS/ADMIN/USERS/TEACHERS/CLASS/STUDENTS.html')



def STUDENT_view(request):

    return render(request, 'USERS/STUDENT/Student_page.html')

def STUDENT_ALPHABET_view(request):

    return render(request, 'USERS/STUDENT/ALPHABET/ALPHABET.html')


def STUDENT_BOOKS_view(request):

    return render(request, 'USERS/STUDENT/BOOKS/BOOKS.html')


def STUDENT_TEST_view(request):

    return render(request, 'USERS/STUDENT/TEST/TEST.html')

def STUDENT_WORDS_view(request):

    return render(request, 'USERS/STUDENT/WORDS/WORDS.html')




def TEACHER_view(request):

    return render(request, 'USERS/TEACHER/Teacher_page.html')



def TEACHER_CLASS_view(request):

    return render(request, 'USERS/TEACHER/CLASS/')


def TEACHER_STUDENT_REGISTRATION_view(request):

    return render(request, 'USERS/TEACHER/CLASS/STUDENT_REGISTRATION/Student_Register_Page.html')


def TEACHER_STUDENT_REGISTRATION_REGISTER_SUCCESS_view(request):

    return render(request, 'USERS/TEACHER/CLASS/STUDENT_REGISTRATION/REGISTER SECCSES/SECSES.html')


def TEACHER_CLASS_STUDENTS_view(request):

    return render(request, 'USERS/TEACHER/CLASS/STUDENTS/')

def TEACHER_CLASS_STUDENTS_STUDENT_view(request):

    return render(request, 'USERS/TEACHER/CLASS/STUDENTS/STUDENT/')

def TEACHER_CLASS_STUDENTS_STUDENT_DISPLAY_view(request):

    return render(request, 'USERS/TEACHER/CLASS/STUDENTS/STUDENT/DISPLAY/')

def TEACHER_CLASS_STUDENTS_STUDENT_DATA_view(request):

    return render(request, 'USERS/TEACHER/CLASS/STUDENTS/STUDENT/STUDENT_DATA/')

def TEACHER_CLASS_STUDENTS_STUDENT_PAGE_view(request):

    return render(request, 'USERS/TEACHER/CLASS/STUDENTS/STUDENT/STUDENT_PAGE/')














def contact(request):
    return render(request, 'TEST_APP/SITE_TEST_2.html' , {'content':['content ','content']}) #dictionaries



'''