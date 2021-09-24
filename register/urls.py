from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('form', views.form, name='form'),
    path('sur_status', views.sur_status, name='sur_status')
]