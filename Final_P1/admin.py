from django.contrib import admin
from .models import studentInfo, favorite, clubs

# Register your models here.

admin.site.register(studentInfo)
admin.site.register(favorite)
admin.site.register(clubs)