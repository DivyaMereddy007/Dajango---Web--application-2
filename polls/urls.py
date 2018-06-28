from django.urls import path
from . import views

#app_name='polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    #try
    path('some_view/', views.some_view, name='some_view'),
    path('some_view1/', views.some_view1, name='some_view1'), 
]
