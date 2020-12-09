from django.urls import path
from . import views
from Final_P1 import views

urlpatterns = [
    path("update_server/", views.update, name="update"),
    path('', views.index, name='index'),
    path('Home', views.index),
    path('Game', views.index2),
    path('Community', views.index3),
    path('About', views.index4),
    path('Profile/Home', views.index),
    path('Profile/Game', views.index2),
    path('Profile/Community', views.index3),
    path('Profile/About', views.index4),
    path('register/', views.register_view, name='register'),
    path('Roster', views.register_view),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('Profile/', views.indexProfile, name='profile'),
    path('Profile/', views.indexProfile, name='index_profile'),
    path('Profile/Form', views.ProfileForm, name='Profile-Form'),
    path('Profile/AddPlayerForm', views.AddPlayerForm, name='PlayerForm'),
    path('Profile/AddInterestForm', views.AddInterestForm, name='InterestForm'),
    path('Profile/FavoriteCharacterForm', views.FavoriteCharacterForm, name='FavoriteCharacterForm'),
]