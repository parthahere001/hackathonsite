from django.urls import path
from hackr import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('getdesc/<int:id>/', views.getdesc, name = 'getdesc'),
    path('getdesc/<int:id>/getgithublink/', views.getgithublink, name='getgithublink'),
    path('getdesc/<int:id>/addsubmissionpage/', views.addsubmissionpage, name='addsubmissionpage'),
    path('getdesc/<int:id>/addsubmissionpage/addsubmission/', views.addsubmission, name='addsubmission'),
    path('addhackathonpage/', views.addhackathonpage, name='addhackathonpage'),
    path('addhackathonpage/addhackathon/', views.addhackathon, name = 'addhackathon'),
    path('login', views.userlogin, name='userlogin'),
    path('logout/', views.userlogout, name='userlogout'),
    path('userregister/', views.userregister, name='userregister'),
] 