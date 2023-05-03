from django.shortcuts import render
from .models import PHdb

# Create your views here.
def pn(request):
    pns = PHdb.objects.all()
    template = 'index.html'
    data = {
        'pns': pns,
    }
    return render(request, template, data)