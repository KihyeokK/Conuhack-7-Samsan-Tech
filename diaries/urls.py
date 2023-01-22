from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('diaries/', views.diary_list, name="diary-list"),
    path('diaries/<int:pk>/', views.snippet_detail, name="diary-detail"),
    path('users/', views.diary_list, name="user-list"),
    path('users/<int:pk>/', views.snippet_detail, name="user-detail"),
    # If you open a browser and navigate to the browsable API at the moment,
    #  you'll find that you're no longer able to create new code snippets. 
    # In order to do so we'd need to be able to login as a user.
    path('api-auth/', include('rest_framework.urls')),
]

# We don't necessarily need to add these extra url patterns in, but it gives us a simple,
# clean way of referring to a specific format.
urlpatterns = format_suffix_patterns(urlpatterns)