from django.contrib import admin
from .models import User, Image , Profile

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)