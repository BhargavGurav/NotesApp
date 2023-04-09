from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('collect_note/', views.collect_note, name='collect_note'),
    path('upload_note/', views.upload_note, name='upload_note'),
    path('registration/', views.registration, name='registration'),

]