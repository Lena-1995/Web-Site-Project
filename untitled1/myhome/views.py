from django.shortcuts import render
from django.http import HttpResponse
from .models import LogUser
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import TeacherUserForm,StudentUserForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from PyPDF2 import PdfFileReader, PdfFileWriter
from django.core.files.storage import FileSystemStorage
# Create your views here.
'''
def Teacherform(request):
    if request.method == "POST":
        form = Teacherform(request.POST)
        if form.is_valid():
            new_form=form.save()
            return render(request, 'Site_App/SITE_TEST_1.html')

    else:
        form=Teacherform()
    c={'form':form}


    return render(request, 'Site_App/SITE_TEST_1.html',c)
    # return HttpResponse('<h1>This is my home page</h1>')

def StudentForm(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_form=form.save()
            return render(request, 'Site_App/SITE_TEST_1.html')

    else:
        form=StudentForm()
    c={'form':form}


    return render(request, 'Site_App/SITE_TEST_1.html',c)
    # return HttpResponse('<h1>This is my home page</h1>')

def BooksForm(request):
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            new_form=form.save()
            return render(request, 'Site_App/SITE_TEST_1.html')

    else:
        form=BooksForm()
    c={'form':form}


    return render(request, 'Site_App/SITE_TEST_1.html',c)
    # return HttpResponse('<h1>This is my home page</h1>')


def WordsForm(request):
    if request.method == "POST":
        form = WordsForm(request.POST)
        if form.is_valid():
            new_form=form.save()
            return render(request, 'Site_App/SITE_TEST_1.html')

    else:
        form=WordsForm()
    c={'form':form}


    return render(request, 'Site_App/SITE_TEST_1.html',c)
    # return HttpResponse('<h1>This is my home page</h1>')


'''








def register(request):
    if request.method == "POST":
        form = TeacherUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("HOME")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "LOGIN/Register.html",
                          context={"form":form})

    form = TeacherUserForm
    return render(request = request,
                  template_name = "LOGIN/Register.html",
                  context={"form":form})


@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("HOME")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "LOGIN/Login.html",
                    context={"form":form})















def HOME_view(request):

    return render(request,'Project_site.html',{})


def Settings_view(request):
    return render(
        request,
        'News.html',
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

def ADMIN_Settings_view(request):
    return render(
        request,
        'USERS/ADMIN/Settings.html',
    )

def ADMIN_Data_view(request):
    return render(
        request,
        'USERS/ADMIN/Data.html',
    )

def ADMIN_Mess_view(request):
    return render(
        request,
        'USERS/ADMIN/Mess.html',
    )
def ADMIN_Rating_view(request):
    return render(
        request,
        'USERS/ADMIN/Rating.html',
    )

def ADMIN_Users_view(request):
    return render(
        request,
        'USERS/ADMIN/Users.html',context = {"Users":User.objects.all}
    )

def TEACHER_Users_view(request):
    return render(
        request,
        'USERS/TEACHER/Users.html',context = {"Users":User.objects.all}
    )

def TEACHER_Chat_view(request):
    return render(
        request,
        'USERS/TEACHER/Chat.html',
    )

def TEACHER_Class_view(request):
    return render(
        request,
        'USERS/TEACHER/Class.html',
    )

def TEACHER_Data_view(request):
    return render(
        request,
        'USERS/TEACHER/Data.html',
    )

def TEACHER_Settings_view(request):
    return render(
        request,
        'USERS/TEACHER/Settings.html',
    )


def STUDENT_Alphabet_view(request):

    return render(
        request,
        'USERS/STUDENT/Alphabet.html',{"FILE":GetImg()}
    )

def STUDENT_Books_view(request):
    return render(
        request,
        'USERS/STUDENT/Books.html',context = {"BOOKS":Books.objects.all}
    )
def STUDENT_Test_view(request):
    return render(
        request,
        'USERS/STUDENT/Test.html',
    )
def STUDENT_Words_view(request):
    return render(
        request,
        'USERS/STUDENT/Words.html',context = {"WORDS":Words.objects.all}
    )


def TEST_LIST_view(request):
    return render(
        request,
        'USERS/TEACHER/Data/Word_list.html',context = {"TEST":StudentTest.objects.all}
    )


def TEACHER_Words_view(request):
    return render(
        request,
        'USERS/TEACHER/Data/Word_list.html',context = {"WORDS":Words.objects.all}
    )
def TEACHER_Book_view(request):
    return render(
        request,
        'USERS/TEACHER/Data/Book_list.html',context = {"BOOKS":Books.objects.all}
    )
def ADD_BOOK_view(request):
    if request.method == 'POST':
        form = Book_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('HOME')
    else:
        form = Book_Form()
    return render(request, 'USERS/TEACHER/DATA/Add_Book.html', {
        'form': form
    })





def ADD_WORD_view(request):
    if request.method == 'POST':
        form = Word_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('HOME')
    else:
        form = Word_Form()
    return render(request, 'USERS/TEACHER/DATA/Add_word.html', {
        'form': form
    })


    return render(request, 'USERS/TEACHER/DATA/Add_word.html',c)


def ADD_Class_view(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            new_form=form.save()
            return redirect('HOME')

    else:
        form=ClassForm()
    c={'form':form}


    return render(request, 'USERS/TEACHER/CLASS/Add_Class.html',c)


def ADD_TEST_view(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            new_form=form.save()
            return redirect('HOME')

    else:
        form=TestForm()
    c={'form':form}


    return render(request, 'USERS/TEACHER/DATA/ADD_TEST.html',c)

def ADD_USER_view(request):
    if request.method == "POST":
        form = StudentUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            return redirect("HOME")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "LOGIN/Register.html",
                          context={"form":form})

    form = StudentUserForm
    return render(request = request,
                  template_name = "LOGIN/Register.html",
                  context={"form":form})







def Img():
    word = input("Enter the charecther that you uwant to learn (a-z,0-9):")
    dictionary = {
        1: "0",
        2: "1",
        3: "2",
        4: "3",
        5: "4",
        6: "5",
        7: "6",
        8: "7",
        9: "8",
        10: "9",
        11: "a",
        12: "b",
        13: "c",
        14: "d",
        15: "e",
        16: "f",
        17: "g",
        18: "h",
        19: "i",
        20: "j",
        21: "k",
        22: "l",
        23: "m",
        24: "n",
        25: "o",
        26: "p",
        27: "q",
        28: "r",
        29: "s",
        30: "t",
        31: "u",
        32: "v",
        33: "w",
        34: "x",
        35: "y",
        36: "z"
    }
    for key, value in dictionary.items():
        if word == value:
            return key - 1


def GetImg():

    PdfFile = open("media/Local_media/alphabet.pdf", "rb")
    pdf_reader = PdfFileReader(PdfFile)
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf_reader.getPage(Img()))
    newFile = open('media/Local_media/newFile.pdf', 'wb')
    pdf_writer.write(newFile)
    newFile.close()
    PdfFile.close()

