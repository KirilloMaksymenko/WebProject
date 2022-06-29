
from django.urls import path
from . import views
from random import randint

urlpatterns = [
    ###___Local___###
    path('', views.index, name='home'),
    path('my-board/', views.index, name='home'),
    path('my-board/create-notes/', views.create.as_view(), name='create'),
    path('my-board/<int:pk>/views/',views.view_note, name='views-notes'),
    path('my-board/<int:pk>/views/delete',views.delete_note, name='delete-notes'),

    ###___Server___###
    path('server-board/', views.index_server, name='server-board-view'),
    path('server-board/create-notes/', views.server_create.as_view(), name='server-create'),
    path(f'server-board/account/<int:pk>/views/',views.server_account_view.as_view(), name='server-account-views'),
    path(f'server-board/<int:pk>/views/',views.server_view_note.as_view(), name='server-views-notes'),
    path('server-board/<int:pk>/views/delete/',views.server_delete_note.as_view(), name='server-delete-notes'),
    path(f'server-board/<int:pk>/views/reactions/',views.server_reaction_view, name='server-views-reactions'),


    ###___Account___###
    path('account/login/', views.LoginUser.as_view(), name='login-page'),
    path('account/register/', views.RegisterUser.as_view(), name='regist-page'),
    path('account/logout/', views.LogoutUser.as_view(), name='logout-page'),
    path('account/profile/', views.ProfileUser.as_view(), name='profile-page'),
    path('account/profile/<int:pk>/edit/', views.EditProfil.as_view(), name='profile-edit-page'),

]
