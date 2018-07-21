from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile
from tracker.models import Weight

admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class WeightInline(admin.StackedInline):
    model = Weight
    can_delete = False
    extra = 0

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, WeightInline)


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
