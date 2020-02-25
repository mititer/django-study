from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.pivot, name='pivot'),
    path('data', views.pivot_data, name='pivot_data')
]