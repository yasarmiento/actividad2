from django.urls import path
from apps.vehiculo import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('vehiculo/create/', views.create, name = 'vcreate'),
    path('vehiculo/update/<int:id>', views.update, name ='vupdate'),
    path('vehiculo/delete/<int:id>', views.delete, name = 'vdelete'),
    path('tipovehiculo', views.iniciotv, name= 'tvinicio'),
    path('tipovehiculo/create/', views.createtv, name = 'tvcreate'),
    path('tipovehiculo/update/<int:id>', views.updatetv, name ='tvupdate'),
    path('tipovehiculo/delete/<int:id>', views.deletetv, name = 'tvdelete'),
]
