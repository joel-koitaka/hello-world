from django.contrib import admin
from account.models import UserProfile, Article

# Register your models here.
admin.site.register(UserProfile)  # userprofile is the name of the model
admin.site.register(Article)