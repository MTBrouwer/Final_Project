from django import forms
from .models import Player,PlayerInterest,PlayerFavoriteCharacter

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class InterestForm(forms.ModelForm):
    class Meta:
        model = PlayerInterest
        fields = '__all__'

class FavoriteCharacterForm(forms.ModelForm):
    class Meta:
        model = PlayerFavoriteCharacter
        fields = '__all__'

