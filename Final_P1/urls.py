from django.urls import path
from . import views
urlpatterns = [
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
    path('Roster/Overwatch', views.indexO),
    path('Roster/FIFA', views.indexF),
    path('Roster/SSBU', views.indexS),
    path('Roster/Hearthstone', views.indexH),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('Profile/', views.indexProfile, name='profile'),
    path('Profile/Form', views.indexProfile, name='Profile-Form'),
    ##UserProf
    path('', views.view_profile, name='view_profile'),
    path('add', views.create_profile, name='create_profile'),
    path('update/<int:id>', views.update_profile, name='update_profile'),
]