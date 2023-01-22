from .models import Diary
from .serializers import DiarySerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
# to create a single entry point to our API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse # to return fully-qualified URLs; 


# converting generic views to function-based views
from rest_framework import status


@api_view(['GET', 'POST'])
def diary_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        diaries = Diary.objects.all()
        serializer = DiarySerializer(diaries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        diary = Diary.objects.get(pk=pk)
    except Diary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiarySerializer(diary)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiarySerializer(diary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        diary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def diary_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'diaries': reverse('diary-list', request=request, format=format)
    })