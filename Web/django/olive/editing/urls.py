from django.urls import path
from . import views


urlpatterns = [
    path('', views.portfolio_details, name='portfolio-details'),
    path('insert_students/', views.insert_students, name='insert-students'),
    path('student/', views.students, name='student')


]