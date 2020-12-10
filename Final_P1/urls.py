from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Home', views.index),
    path('Game', views.game),
    path('Community', views.community),
    path('About', views.about),
    path('Profile/Home', views.index),
    path('Profile/Game', views.game),
    path('Profile/Community', views.community),
    path('Profile/About', views.about),
    path('register/', views.register_view, name='register'),
    path('Roster', views.register_view),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('Profile/', views.indexProfile, name='profile'),
    path('Profile/', views.indexProfile, name='index_profile'),
    path('Profile/Form', views.ProfileForm, name='Profile-Form'),
    path('Profile/studentInfoForm', views.AddPlayerForm, name='studentInfoForm'),
    path('Profile/studentInterestForm', views.InterestForm, name='clubForm'),
    path('Profile/favorite', views.favorite, name='favorite'),
    path('Profile/Delete<int:id>', views.delete, name='Delete-StudentForm'),

]