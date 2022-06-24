
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Management.Forms import RegisterForm
from Management.models import Register


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,"menu.html")
def book(request):
    myForm=RegisterForm()
    if request.method=='POST':
        name=request.POST['name']
        seat=request.POST['seat']
        date=request.POST['date']
        new_Data=Register(Name=name,Seat=seat,Date=date)
        new_Data.save()
        form=RegisterForm(request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect('book')
    return render(request,'book.html')