from django.urls import path
from . import views

urlpatterns = [
    path('static_array/', views.my_static_array, name='static_array'),
]
