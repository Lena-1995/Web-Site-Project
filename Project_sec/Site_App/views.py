from django.shortcuts import render
from .forms import SingInForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.

def TEST_FUN(request):

    form = SingInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'Site_App/SITE_TEST_1.html')
    # return HttpResponse('<h1>This is my home page</h1>')


'''

def contact(request):
    return render(request, 'TEST_APP/SITE_TEST_2.html' , {'content':['content ','content']}) #dictionaries

'''