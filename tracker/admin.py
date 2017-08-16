from django.contrib import admin
from .models import Workout, Sets, Exercise, Muscle, Weight


admin.site.register(Sets)
admin.site.register(Exercise)
admin.site.register(Muscle)
admin.site.register(Weight)


class SetsInline(admin.TabularInline):
    model = Sets
    extra = 0

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator')
    fields = ['name', 'creator']
    inlines = [SetsInline]
