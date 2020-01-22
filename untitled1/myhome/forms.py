from django.forms import ModelForm,TextInput
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TeacherUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(TeacherUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.is_staff = True
            user.save()
        return user



class StudentUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(StudentUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.is_staff = False
            user.save()
        return user









class Book_Form(forms.ModelForm):
    class Meta:
        model = Book
        fields=('name','book')


class Word_Form(forms.ModelForm):
    class Meta:
        model = Words
        fields=('name','img')














class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = [""]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = [""]





class WordsForm(forms.ModelForm):
    class Meta:
        model = Words
        exclude = [""]


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        exclude = [""]

class TestForm(forms.ModelForm):
    class Meta:
        model = StudentTest
        exclude = [""]

