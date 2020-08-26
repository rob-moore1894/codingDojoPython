from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main', views.main),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('wish_items/create', views.createItemView),
    path('wish_items/<int:itemId>', views.viewItem),
    path('create-item', views.createItem),
    path('delete/<int:itemId>', views.delete),
    path('addItem/<int:itemId>', views.addItem),
    path('removeItem/<int:itemId>', views.removeItem),
]