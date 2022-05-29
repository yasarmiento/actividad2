from django.urls import path
from apps.marca import views

urlpatterns = [
    path('marca', views.minicio, name= 'minicio'),
    path('marca/create/', views.mcreate, name = 'mcreate'),
    path('marca/update/<int:id>', views.mupdate, name ='mupdate'),
    path('marca/delete/<int:id>', views.mdelete, name = 'mdelete'),
]
