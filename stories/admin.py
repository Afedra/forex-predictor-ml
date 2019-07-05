from django.contrib import admin
from .models import *

class StoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'published_date','created_date')

admin.site.register(Story, StoryAdmin)
