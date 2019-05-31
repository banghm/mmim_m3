from django.conf.urls import url, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'elections'

urlpatterns = [
   path('index/', views.index, name='index'),
   path('register/', views.register, name='register'),
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('contract/', views.Contract, name='contract'),
   path('show/contract/<p_id>/<id>', views.showContract, name='show-contract'),
   path('show/contract/', views.showMyContract, name='show-my-contract')

]