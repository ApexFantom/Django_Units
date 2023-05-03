from django.shortcuts import render, redirect
from .forms import StudentsForm
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, home.")

def home(rrequest):
    return HttpResponse("Hello, home.")
def dom(rrequest):
    return HttpResponse("Hello, dom.")

def StudentsFormUpdate(request):
    error = ""
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'е верный ip'

    form = StudentsForm()
    data ={
        'form':form,
        'error':error,
    }
    return render(request, 'getForm.html', data)
