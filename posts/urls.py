# Django
from django.urls import path

# View
from . import views


app_name = 'posts'

urlpatterns = [
    path(
        route='',
        view=views.Home.as_view(),
        name='home'
    ),
    path(
        route='about/',
        view=views.About.as_view(),
        name='about'
    ),
    path(
        route='post',
        view=views.ListPosts.as_view(),
        name='home_login_posts'
    ),
    path(
        route='create/new/posts/',
        view=views.CreatePostsView.as_view(),
        name='new_posts'
    ),
    path(
        route='contact',
        view=views.ContactView.as_view(),
        name='contact'
    ),
    path(
        route='register',
        view=views.RegisterBetaView.as_view(),
        name='register'
    ),
]