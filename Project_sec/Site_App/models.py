from django.db import models

import datetime
from django.utils import timezone



# Create your models here.


class SingIn(models.Model):
    UserName = models.CharField(max_length=64)
    UserPass = models.CharField(max_length=64)
    Email = models.EmailField()





class SITE_SETTINGS(models.Model):
    color=models.CharField(max_length=8)

    Teacher_url = models.URLField()
    Student_url = models.URLField()

    def __str__(self):
        return self

    class Meta:
        verbose_name = "SITE_SETTINGS"
        verbose_name_plural = "SITE_SETTINGS"



class BOOKS(models.Model):
    Book_Name=models.CharField(max_length=128)
    Book=models.FileField()
    def __str__(self):
        return self.Book_Name

    class Meta:
        verbose_name = "BOOK"
        verbose_name_plural = "BOOKS"



class PICTURES(models.Model):
    PIC={'HOME_PAGE':models.ImageField(upload_to='Media')}



    class Meta:
        verbose_name = "PICTUR"
        verbose_name_plural = "PICTURES"


class WORDS(models.Model):
    Word=models.CharField(max_length=128)
    Word_pic=models.ImageField(upload_to='Media/words')



    def __str__(self):
        return self.Word

    class Meta:
        verbose_name = "WORD"
        verbose_name_plural = "WORDS"


class TEST(models.Model):
    TEST_NAME = models.CharField(max_length=128)

    class question(models.Model):
        text=models.CharField(max_length=128)#need to be spleated

    def __str__(self):
        return self.TEST_NAME

    class Meta:
        verbose_name = "WORD"
        verbose_name_plural = "WORDS"



class USERS(SITE_SETTINGS):
    Admin=False
    Teacher=False

    UserName = models.CharField(max_length=64)
    UserPass = models.CharField(max_length=64)
    Email = models.EmailField()

    def __str__(self):
        return self.UserName

    class Meta:
        verbose_name = "USER"
        verbose_name_plural = "USERS"


class ADMIN(USERS):
    Admin=True

    def __str__(self):
        return self.Admin

    class Meta:
        verbose_name = "ADMIN"
        verbose_name_plural = "ADMIN"


class TEACHER(USERS):
    Teacher = True

    class CLASS(models.Model):
        CLASS_NAME = models.CharField(max_length=64)

        class STUDENT(USERS):
            Student = True

            def __str__(self):
                return self.STUDENT

            class Meta:
                verbose_name = "STUDENT"
                verbose_name_plural = "STUDENTS"

        def __str__(self):
            return self.CLASS_NAME

        class Meta:
            verbose_name = "CLASS"
            verbose_name_plural = "CLASSES"

    def __str__(self):
        return self.Teacher

    class Meta:
        verbose_name = "TEACHER"
        verbose_name_plural = "TEACHERS"




























'''
class SingIn(models.Model):
    name=models.CharField("Name",max_length=64)
    
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name="name"
        verbose_name_plural="names"







'''