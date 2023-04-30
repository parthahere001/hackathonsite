from django.shortcuts import render
from .models import hackathonsModel, hackersModel

def homepage(request):
    allhackathons = hackathonsModel.objects.all()
    context = {
       'allhackathons' : allhackathons 
    }
    return render(request, 'index.html', context)


def getdesc(request, id):
   hackathon = hackathonsModel.objects.get(id = id)
   context = {
      'hackathon' : hackathon
   }
   return render(request, 'descpage.html', context)