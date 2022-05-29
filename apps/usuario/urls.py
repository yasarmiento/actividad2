from django.urls import path
from apps.usuario import views

urlpatterns = [
    path('usuario/inicio', views.uinicio, name= 'uinicio'),
    path('usuario/create/', views.ucreate, name = 'ucreate'),
    path('usuario/update/<int:id>', views.uupdate, name ='uupdate'),
    path('usuario/delete/<int:id>', views.udelete, name = 'udelete'),
    path('ventas/inicio', views.ventinicio, name= 'ventinicio'),
    path('ventas/create/', views.ventcreate, name = 'ventcreate'),
    path('ventas/update/<int:id>', views.ventupdate, name ='ventupdate'),
    path('ventas/delete/<int:id>', views.ventdelete, name = 'ventdelete'),
    path('vehiculosventas/inicio', views.vehinicio, name= 'vehinicio'),
    path('vehiculosventas/create/', views.vehcreate, name = 'vehcreate'),
    path('vehiculosventas/update/<int:id>', views.vehupdate, name ='vehupdate'),
    path('vehiculosventas/delete/<int:id>', views.vehdelete, name = 'vehdelete'),
]