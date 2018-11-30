from django.shortcuts import render
from testapp.models import Jobs

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def hyd_jobs(request):
    hydjobs=Jobs.objects.all()
    return render(request,'testapp/hydjobs.html',{'hydjobs':hydjobs})
def blore_jobs(request):
    blorejobs=Jobs.objects.all()
    return render(request,'testapp/blore.html',{'blorejobs':blorejobs})
