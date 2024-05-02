from django.urls import path
from mitha import views
urlpatterns = [
    path('', views.fill, name="fill"),
]
