from django.urls import path, include
from .views import home, getdata, about,docs
app_name = 'mainapp'

urlpatterns = [
    path('',home,name='home'),
    path('getdata/<str:input>',getdata,name='getdata'),
    path('about/',about,name='about'),
    path('docs/',docs,name='doc'),
]
