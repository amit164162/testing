from django.urls import path
from . import views

urlpatterns =[
    path('student', views.student, name='student'),
    path('teacher',views.teacher, name='teacher'),
]