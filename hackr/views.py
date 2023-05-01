from django.shortcuts import render, redirect
from .models import hackathonsModel, hackersModel, submissionModel
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.models import User

def homepage(request):
   print("##########################")
   print(request.user)
   if request.user != None:
      allhackathons = hackathonsModel.objects.all()
      context = {
        'allhackathons' : allhackathons 
      }
      return render(request, 'index.html', context)
   else:
       return redirect('userlogin')
  


def getdesc(request, id):
   hackathon = hackathonsModel.objects.get(id = id)
   context = {
      'hackathon' : hackathon
   }
   return render(request, 'descpage.html', context)

def getgithublink(request, id):
   usr = request.user
   hacker = hackersModel.objects.get(hackerid = usr)
   hackathon = hackathonsModel.objects.get(id = id)
   return redirect(hackathon.githubrepolink)
   
def addhackathonpage(request):
   return render(request, 'addhackathonpage.html')

def addhackathon(request):
   new_user = request.user
   hackr = hackersModel.objects.get(hackerid=new_user)
   title = request.POST['title']
   tagline = request.POST['tagline']
   description = request.POST['description']
   hackathon_image = request.FILES['hackathon_image']
   typeofsubmission = request.POST['submissiontype']
   rewardprize = request.POST['rewardprize']
   startdate = request.POST['startdate']
   enddate = request.POST['enddate']
   githublink = request.POST['githublink']
   otherlink = request.POST['otherlink']
   print(hackr.name)
   newhackathon = hackathonsModel(title=title, tagline=tagline, description=description, hackathon_image=hackathon_image, type_of_submission=typeofsubmission, reward_prize=rewardprize, startdatetime=startdate, enddatetime=enddate, oragniser=hackr.name, githubrepolink=githublink, otherlinks=otherlink)
   newhackathon.save()
   return HttpResponseRedirect(reverse('homepage')) 

def addsubmissionpage(request, id):
   hackr = hackersModel.objects.get(hackerid=request.user)
   hackathon = hackathonsModel.objects.get(id=id)
   try:
      madesubmission = submissionModel.objects.get(hkr = hackr, hkthn = hackathon)
      return render(request, 'madesubmission.html')
   except ObjectDoesNotExist:
      
      showlink=1
      if (hackathon.type_of_submission=="link" or hackathon.type_of_submission=="Link"):
         showlink=1
      elif (hackathon.type_of_submission=='image' or hackathon.type_of_submission=='Image'):
         showlink=2
      else:
         showlink=3
      context={
         'showlink' : showlink,
         'id' : id
      }
      return render(request, 'addsubmissionpage.html', context)

   
def addsubmission(request, id):
      curr_user = request.user
      hackr = hackersModel.objects.get(hackerid=curr_user)
      title = request.POST['title']
      summary = request.POST['summary']
      hackthon = hackathonsModel.objects.get(id=id)
      if (hackthon.type_of_submission == "link" or hackthon.type_of_submission == "Link"):
         link = request.POST['link']
         newsubmission = submissionModel(name=title, summary=summary, hkr = hackr, hkthn = hackthon, submission_link = link)
      elif (hackthon.type_of_submission == "image" or hackthon.type_of_submission == "Image"):
         pic = request.FILES['uploadimage']
         newsubmission = submissionModel(name=title, summary=summary, hkr = hackr, hkthn = hackthon, submission_link = "")
      else:
         ufile = request.FILES['uploadfile']
         newsubmission = submissionModel(name=title, summary=summary, hkr = hackr, hkthn = hackthon, submission_link = "", submission_file = ufile)
      newsubmission.save()
      return HttpResponseRedirect(reverse('homepage')) 


def userlogin(request):
  if request.method=="POST":
        # Get the post parameters
      loginusername=request.POST['loginusername']
      loginpassword=request.POST['loginpassword']
      user=authenticate(username= loginusername, password= loginpassword)
      if user is not None:
          login(request, user)
          messages.success(request, "Successfully Logged In")
          return redirect("homepage")
      else:
          messages.error(request, "Invalid credentials! Please try again")
          return redirect("userlogin")
  return render (request,'log.html')


def userlogout(request):
    logout(request)
    return redirect('userlogin')

def userregister(request):
   if request.user is not None:
      form = CreateUserForm()
      if request.method == 'POST':
         form = CreateUserForm(request.POST)
         if form.is_valid():
            new_user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            login(request, new_user)
            name = new_user.get_username()
            newhacker = hackersModel(name = name, hackerid = request.user, )
            newhacker.save()
            return redirect('homepage')
      context = {'form':form}
      return render(request, 'userregister.html',context)
   else:
      return redirect('homepage')


