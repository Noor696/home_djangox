from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    # I would to add extra filed and show it in admin bage
    fieldsets = UserAdmin.fieldsets + (('Contact information',{'fields':('phone_number',)}),)

admin.site.register(CustomUser, CustomUserAdmin)