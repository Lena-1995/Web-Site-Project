from django.db import models
from django.contrib.auth.forms import UserChangeForm


# Create your models here.

class TEST(models.Model):

    Title=models.CharField(max_length=64),
    post=models.TextField(),

    def __str__(self):
        return self.Title


class LogUser(models.Model):

    def __init__(self):
        self.name=None
        self.user_name=None

    def __str__(self):
        return self.name

    def getuser(self):
        return self.user_name

    def login(self, per=None,user=None):
        if str(per) == "ADMIN" or "TEACHER" or "STUDENT":
            self.name = str(per)
            self.user_name=str(user)

    def logout(self):
        self.name=None
        self.user_name=None


class Sitesetiings(models.Model):
    def __init__(self):
        bgc = "#1abc9c"
        #body student
        color = "white"
        font = "Arial"


    def __str__(self):
        return "SiteSettings"


class Teacher(models.Model):
    name=models.CharField(max_length=64)
    password=models.CharField(max_length=64)
    email=models.EmailField(max_length=254)

    def __str__(self):
        return self.name

    def getname(self):
        return self.name

    def getpassword(self):
        return self.password

    def getemail(self):
        return self.email


class Student(Sitesetiings):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    classname=models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def getname(self):
        return self.name

    def getpassword(self):
        return self.password




class Books(models.Model):
    name=models.CharField(max_length=256)
    book=models.FileField(upload_to='media/books/')

    def __str__(self):
        return self.name




class Words(models.Model):
    name=models.CharField(max_length=256)
    img=models.ImageField(upload_to='media/words/')

    def __str__(self):
        return self.name





class StudentTest(models.Model):
    name=models.CharField(max_length=64)
    q1 = models.TextField(max_length=128)
    q2 = models.TextField(max_length=128)
    q3 = models.TextField(max_length=128)
    q4 = models.TextField(max_length=128)
    q5 = models.TextField(max_length=128)

    def __str__(self):
        return self.name

