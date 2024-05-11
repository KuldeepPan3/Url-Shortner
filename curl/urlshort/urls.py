from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shorturls', views.shorturls, name='shorturls'),
    path('<str:shorturl>', views.redirecturl, name='redirecturl')

]