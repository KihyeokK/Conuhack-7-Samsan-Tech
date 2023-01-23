from .models import Diary
from .serializers import DiarySerializer, UserSerializer
from django.contrib.auth.models import User
# to create a single entry point to our API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse # to return fully-qualified URLs; 
# converting generic views to function-based views
from rest_framework import status
# google_cloud_ocr
import os
import io
from google.cloud import vision
import openai


fpath = "/Users/joekimkh/Desktop/sad.jpg"

def GPTchat(text):
        # Replace "YOUR_API_KEY" with your OpenAI API key
        openai.api_key = "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"

        prompt = "in one word and without repeating the question, what is the emotion behind this text " + text

        # Generate a response from the model
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        # Print the response
        response_text = completions.choices[0].text
        return response_text
def google_cloud_ocr(path):
    """Detects document features in an image."""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/joekimkh/Downloads/hackthon23-df6b6798f88b.json"
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return response.full_text_annotation.text


@api_view(['GET', 'POST'])
def diary_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        diaries = Diary.objects.all()
        #diaries = Diary.objects.filter(author=request.user)
        serializer = DiarySerializer(diaries, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # check if the given data is image or text
        #if request.FILES:
        if request.data["content"] == None:
            # access the file using the file path
            text = google_cloud_ocr(fpath)
            request.data["content"] = text
        #request.data.content = request.content
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def diary_detail(request, pk, format=None):
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
def user_list(request):
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
def user_detail(request, pk):
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