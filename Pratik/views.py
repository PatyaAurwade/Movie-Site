from django.shortcuts import render, redirect
from Pratik.models import EventItem
from Pratik.form import MainForm
# Create your views here.
def home(request):
    data = EventItem.objects.all()
    return render(request,'home.html',{'data':data})


def insert(request):
    form = MainForm(request.POST)
    if form.is_valid():
        form.save()
        redirect('home')
    return render(request,'insert.html',{'form':form},)