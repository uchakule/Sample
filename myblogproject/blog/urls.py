# blog/urls.py

from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import YourSignUpView, YourViews


urlpatterns = [
    # Other app-specific URLs

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', YourSignUpView.as_view(), name='signup'),
    path('', YourViews.post_list, name='post_list'),
    path('post/<int:pk>/', YourViews.post_detail, name='post_detail'),
    path('post/new/', YourViews.post_new, name='post_new'),
    path('post/<int:pk>/edit/', YourViews.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', YourViews.add_comment, name='add_comment'),
]
