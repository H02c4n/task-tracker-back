from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('all/', views.tasks, name='tasks'),
    path('<int:id>/', views.get_put_delete_one, name='one')
]