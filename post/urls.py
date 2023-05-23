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
        route='post',
        view=views.ListPosts.as_view(),
        name='index'
    ),
    path(
        route='create/new/post/',
        view=views.CreatePostView.as_view(),
        name='new_post'
    ),
]