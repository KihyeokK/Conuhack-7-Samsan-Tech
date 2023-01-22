from .models import Diary
from .serializers import DiarySerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
# to create a single entry point to our API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse # to return fully-qualified URLs; 


class DiaryList(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # to modify how the instance save is managed, and handle any information that
    # is implicit in the incoming request or requested URL
    def perform_create(self, serializer):
        # The create() method of our serializer will now be passed an additional 'author' field, 
        # along with the validated data from the request.
        serializer.save(author=self.request.user)
    def get_queryset(self):
        return Diary.objects.filter(author=self.request.user)
    

class DiaryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_queryset(self):
        return Diary.objects.filter(author=self.request.user)
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'diaries': reverse('diary-list', request=request, format=format)
    })