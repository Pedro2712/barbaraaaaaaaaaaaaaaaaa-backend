from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/notes/<int:note_id>/', views.api_note),
    path('api/notes/', views.note_user),
    path('api/notes/all/', views.api_note_all),
    path('api/token/', views.api_get_token),
    path('adiciona/', views.adiciona, name='adiciona'),
    path('cadastra/', views.cadastra, name='cadastra'),
    path('favorita/', views.favorita, name='favorita'),
]
