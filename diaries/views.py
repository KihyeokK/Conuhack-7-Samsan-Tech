from .models import Diary
from .serializers import DiarySerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
# to create a single entry point to our API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse # to return fully-qualified URLs; 
# react
"""
from django.shortcuts import render
from rest_framework import viewsets

class DiaryViewSet(viewsets.ModelViewSet):
    '''
    viewset provides basic CRUD (create, read, update, delete) functionality
    '''
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
"""

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

# google login

'''
state = getattr(settings, 'STATE')


def google_login(request):
    """
    Code Request
    """
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")


def google_callback(request):
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    client_secret = getattr(settings, "SOCIAL_AUTH_GOOGLE_SECRET")
    code = request.GET.get('code')
    """
    Access Token Request
    """
    token_req = requests.post(
        f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}")
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get('access_token')
    """
    Email Request
    """
    email_req = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
    email_req_status = email_req.status_code
    if email_req_status != 200:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
    email_req_json = email_req.json()
    email = email_req_json.get('email')
    """
    Signup or Signin Request
    """
    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 google이 아니면 에러 발생, 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)
        if social_user.provider != 'google':
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)
        # 기존에 Google로 가입된 유저
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}accounts/google/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)
    except User.DoesNotExist:
        # 기존에 가입된 유저가 없으면 새로 가입
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}accounts/google/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)


class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client

'''