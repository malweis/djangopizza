from django.urls import path
from . import views

app_name = 'pizzeria'

urlpatterns = [

    path('pizzas/', views.pizza_list, name='pizza_list'),
    path('pizzas/<int:pk>/', views.pizza_detail, name='pizza_detail'),
    path('pizzas/create/', views.pizza_create, name='pizza_create'),
    path('ingredientes/', views.ingrediente_list, name='ingrediente_list'),
    path('ingredientes/<int:pk>/', views.ingrediente_detail, name='ingrediente_detail'),
    path('ingredientes/create/', views.ingrediente_create, name='ingrediente_create'),
]
