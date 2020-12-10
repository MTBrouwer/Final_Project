from django import forms
from .models import studentInfo, favorite, clubs


class studentInfoForm(forms.ModelForm):
    class Meta:
        model = studentInfo
        fields = '__all__'


class studentInterestForm(forms.ModelForm):
    class Meta:
        model = favorite
        fields = '__all__'


class clubForm(forms.ModelForm):
    class Meta:
        model = clubs
        fields = '__all__'

# 3 forms first one is  username, grade. and major,
#  second is favorite character, favoirtge game, favorite genra
# Looking for team. Looking for comp, looking for casual
