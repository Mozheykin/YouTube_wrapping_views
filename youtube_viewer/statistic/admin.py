from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'created', 'name', 'count_view', 'avalible',)
    list_display_links = ('video_id', 'created', 'name',)


admin.site.register(Video, VideoAdmin)