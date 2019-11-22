from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import InteropServerForm, MainPageForm
from .models import InteropServer
import json
from .connect import connect
from .parseJson import ParseJsonFile
# Create your views here.

def connectionPage(request):
    if(request.method=='POST'):
        form = InteropServerForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('controlCenter')
    else:
        form = InteropServerForm()
    return render(request,'controlcenter/startConnection.html',{'form':form})

def controlCenter(request):
    if(request.method=='POST'):
        form = MainPageForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            flush_data = data['flush_data']
            # check if InteropServer data needs to be flushed
            if(flush_data == "flush"):
                InteropServer.objects.all().delete()
            return redirect('controlCenter')
    else:
        form = MainPageForm()
    return render(request,'controlcenter/controlCenter.html',{'form': form})

def getMission(request):
    #connect("http://localhost:8000","testuser","testpass")
    server = InteropServer.objects.all()[0]
    #connect(server.url,server.username,server.password)
    mission_file = ParseJsonFile("C:\\Users\\santi\\Desktop\\AUVSI\\AUVSI_System\\AUVSI_System\\controlcenter\\text.json")
    way_points = mission_file.getWayPointList()
    return render(request,'controlcenter/get_mission.html',{'file':mission_file})