from django.urls import path
from . import views

app_name='vieapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('designer/',views.designer,name='designer'),
    path('exhibitor/',views.exhibitor,name='exhibitor'),
    path('model',views.model,name='model'),
    path('sponsor',views.sponsor,name='sponsor'),


]