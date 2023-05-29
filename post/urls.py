# Django
from django.urls import path

# View
from . import views


app_name = 'post'

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
        name='index'
    ),
    path(
        route='create/new/post/',
        view=views.CreatePostView.as_view(),
        name='new_post'
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