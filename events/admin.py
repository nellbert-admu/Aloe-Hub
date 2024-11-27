from django.contrib import admin
from .models import Event

admin.site.register(Event)

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    filter_horizontal = ('tags',)