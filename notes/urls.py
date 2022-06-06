from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/<int:note_id>/', views.note),
    path('notes/', views.note_user),
    path('notes/all/', views.note_all),
    path('token/', views.get_token),
    path('adiciona/', views.adiciona, name='adiciona'),
    path('cadastra/', views.cadastra, name='cadastra'),
    path('favorita/', views.favorita, name='favorita'),
]
