from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import datetime
from .forms import NameForm
from django.utils import timezone
from polls.models import Task


def get_name(request):
    
    return render(request, 'pols/base.html')

def results(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response)

def add(request):
    if request.method == 'POST':
        
        
               
    
    
        task_name = request.POST["your_name"]
        if task_name == '' :
            
            response = "Error."
            return HttpResponse(response)
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ins = Task(task_name=task_name,
                          task_date=time)
                         
        ins.save()
        response = "success."
        return HttpResponse(response)
    else:
        return render(request, "pols/base.html", )
    return render(request, "pols/base.html", )
