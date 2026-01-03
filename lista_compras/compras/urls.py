from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nova/', views.nova_lista, name='nova_lista'),
    path('lista/<int:lista_id>/', views.lista_compras, name='lista_compras'),
    path('lista/<int:lista_id>/', views.deletar_lista, name='deleta'),

    path('lista/<int:lista_id>/comprado/<int:item_id>/', views.marcar_comprado, name='comprado'),
    path('deletar-lista/<int:lista_id>/', views.deletar_lista, name='deletar_lista'),
]    