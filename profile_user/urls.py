# Django
from django.urls import path

# View
from . import views


app_name = 'users'

urlpatterns = [

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='update/user/',
        view=views.UpdateProfileView.as_view(),
        name='update_user'
    ),
    path(
        route='change_password/user/',
        view=views.UserPasswordChangeView.as_view(),
        name='change_password'
    ),
    path(
        route='success/update/user/',
        view=views.SuccessUpdateUser.as_view(),
        name='success'
    ),
    path(
        route='dashboard/user/<int:pk>/',
        view=views.ListDashboarUser.as_view(),
        name='dashboard_user'
    ),
]