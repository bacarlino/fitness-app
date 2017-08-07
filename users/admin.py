from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Profile
from tracker.models import Weight


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class WeightInline(admin.StackedInline):
    model = Weight
    can_delete = False
    extra = 0

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, WeightInline)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
