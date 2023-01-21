from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('diaries/', views.DiaryList.as_view(), name="diary-list"),
    path('diaries/<int:pk>/', views.DiaryDetail.as_view(), name="diary-detail"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    # If you open a browser and navigate to the browsable API at the moment,
    #  you'll find that you're no longer able to create new code snippets. 
    # In order to do so we'd need to be able to login as a user.
    path('api-auth/', include('rest_framework.urls')),
]

"""
path('google/login/', views.google_login, name='google_login'),
path('google/callback/', views.google_callback, name='google_callback'),
path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
"""

# We don't necessarily need to add these extra url patterns in, but it gives us a simple,
# clean way of referring to a specific format.
urlpatterns = format_suffix_patterns(urlpatterns)