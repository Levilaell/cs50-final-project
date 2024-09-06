from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/<int:category_id>', views.post_list, name='category_posts'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.create_comment, name='create_comment'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    path('register/', views.register, name='register'),
    path('login', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
] 