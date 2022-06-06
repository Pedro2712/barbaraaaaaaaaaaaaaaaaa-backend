from hashlib import new
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404, HttpResponse, HttpResponseForbidden, JsonResponse
from sqlalchemy import null
from .models import Note, Favoritos
from .serializers import NoteSerializer, FavSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import time

# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI
def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")


@api_view(['GET', 'POST', 'DELETE'])
def note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()


    if request.method == 'POST':
        new_note_data = request.data
        note.title    = new_note_data['title']
        note.content  = new_note_data['content']
        note.save()

    if request.method == 'DELETE':
        note.delete()
        return Response(status=204)

    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def note_user(request):

    if request.method == "GET":
        notes = Note.objects.filter(user=request.user)
    
    serialized_note = NoteSerializer(reversed(notes), many=True)
    return Response(serialized_note.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def note_all(request):

    if request.method == "POST":
        new_note_data = request.data
        title = new_note_data['title']
        content = new_note_data['content']
        note = Note(title=title, content=content)
        note.save()

    notes = Note.objects.all()
    
    serialized_note = NoteSerializer(reversed(notes), many=True)
    return Response(serialized_note.data)   

@api_view(['POST'])
def get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return JsonResponse({"token":"Não tem acesso"})
    except:
        return HttpResponseForbidden()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def adiciona(request):
    if request.method == 'POST':
        new_note_data = request.data
        content       = new_note_data['content']
        photo         = new_note_data['photo']
        username      = request.user.username
        tempo         = new_note_data['time']
        user          = request.user
        if content!= "":                
            notes = Note(content= content, photo=photo, 
                        username=username, time=tempo,
                	    user= user)
            notes.save()
        return Response(status=200)
    else:
        return HttpResponseForbidden()

@api_view(['POST'])
def cadastra(request):
    try:
        if request.method == 'POST':
            user       = request.data['username']
            email      = request.data['email']
            password   = request.data['password']
            first_name = request.data['first_name']
            last_name  = request.data['last_name']

            if user== '' or email== '' or password== '' or first_name== '' or last_name== '' or not email.endswith('@al.insper.edu.br'):
                return Response(status=404)
            else:
                user = User.objects.create_user(username=user, email=email, password=password, 
                                                first_name=first_name, last_name=last_name)
                user.save()
                return Response(status=200)
        else:
            return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def favorita(request):
    if request.method == 'GET':
        favoritados = Favoritos.objects.filter(user=request.user)

        serialized_fav = FavSerializer(favoritados, many=True)
        return Response(serialized_fav.data)

    if request.method == 'POST':
        new_fav = request.data
        id_card = new_fav['id_card']
        user = request.user

        Fav = Favoritos(id_card= id_card, user= user)
        Fav.save()
        return Response(status=200)

    if request.method == 'DELETE':
        new_fav = request.data
        id_card = new_fav['id_card']
        desFav = Favoritos.objects.filter(id_card=id_card)
        desFav.delete()
        return Response(status=204)