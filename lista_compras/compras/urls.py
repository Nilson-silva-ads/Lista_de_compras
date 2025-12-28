from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_compras, name='lista'),
    path('comprado/<int:item_id>/', views.marcar_comprado, name='comprado'),
    path('deletar/<int:item_id>/', views.deletar_item, name='deletar'),
]    