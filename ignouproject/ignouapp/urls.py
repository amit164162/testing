from django.urls import path

from . import views

urlpattern=[
    path('',views.hello_world_view,name='hello_world_views'),

]