from django.urls import path,include
from firstapp import views

urlpatterns = [
    path('',views.index),
]
