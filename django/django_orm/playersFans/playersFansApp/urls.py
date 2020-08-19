from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls)
    path("", views.index),
    path("createPlayer", views.createPlayer),
    path("players/<int:idPlayer>", views.showPlayer),
    path("addFanToPlayer/<int:idPlayer>", views.addFanToPlayer),
    path("delete/<int:idPlayer>", views.deletePlayer),
    path("edit/<int:idPlayer>", views.editPlayer),
    path("updateplayer/<int:idPlayer>", views.updatePlayer)
    # edit/6
]