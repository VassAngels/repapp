from django.shortcuts import render
from .models import Person
# Create your views here.
def index(request):
    people=Person.objects.all()
    return render(request,'index.html', {'people':people})

def explore(request):
    people=Person.objects.all()
    return render(request,'explore.html', {'people':people})

def index2(request):
    people=Person.objects.all()
    return render(request,'index2.html', {'people':people})
