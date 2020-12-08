from django.contrib import admin
from .models import Player, PlayerInterest, PlayerFavoriteCharacter

# Register your models here.

admin.site.register(Player)
admin.site.register(PlayerInterest)
admin.site.register(PlayerFavoriteCharacter)