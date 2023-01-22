from rest_framework import serializers
from .models import Diary
from django.contrib.auth.models import User

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        #fields = ['content']
        fields ='__all__'

# diaries is a reverse relationship on the User model, it will not be included by default
#  when using the ModelSerializer class, so we needed to add an explicit field for it
class UserSerializer(serializers.ModelSerializer):
    diaries = serializers.PrimaryKeyRelatedField(many=True, queryset=Diary.objects.all())
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = User
        fields = ['id', 'username', 'diaries', 'author']