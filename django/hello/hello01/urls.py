from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.test1),

    # http://127.0.0.1/hello01/

]
