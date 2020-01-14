from django.db import models

# Create your models here.


class SingIn(models.Model):
    UserName = models.CharField(max_length=64)
    UserPass = models.CharField(max_length=64)
    Email = models.EmailField()



'''
class SingIn(models.Model):
    name=models.CharField("Name",max_length=64)
    
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name="name"
        verbose_name_plural="names"







'''