from django.shortcuts import render
#from django.http import HttpResponse
#from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')

def help_page(request):
    help_dict = {'help_insert':"Hello i am the help comment from the appTwo/views.py!"}
    return render(request,'appTwo/help.html',context=help_dict)

def users_page(request):
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error, form invalid")
    return render(request,'appTwo/users.html',{'form':form})



