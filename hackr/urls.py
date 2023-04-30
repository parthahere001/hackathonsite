from django.urls import path
from hackr import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('getdesc/<int:id>/', views.getdesc, name = 'getdesc'),
] 