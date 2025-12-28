from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_compras, name='lista'),
    path('nova/', views.nova_lista, name='nova_lista'),
    path('lista/<int:lista_id>/', view.lista_compras, name='lista_compras'),

    path('lista/<int:item_id>/comprado/<int:item_id>/', views.marcar_comprado, name='comprado'),
    path('lista/<int:lista_id>/deletar/<int:item_id>/', views.deletar_item, name='deletar'),
]    