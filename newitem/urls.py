from django.urls import path
from newitem import views


urlpatterns = [path('', views.index, name='index'),

]