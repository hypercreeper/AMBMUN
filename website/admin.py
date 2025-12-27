from django.contrib import admin
from .models import *

class BoardAdmin(admin.ModelAdmin):
    list_display = ( 'name','id', 'role')
    search_fields = ('name', 'role')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'id' )
    search_fields = ('question',)

class ChairAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'email')
    search_fields = ('name',)
class PagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'email')
    search_fields = ('name',)

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
class MediaItemInline(admin.TabularInline):
    model = MediaItem
    extra = 0  # Number of empty forms to display
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'id', 'album_description')
    search_fields = ('album_name','album_description')
    inlines = [MediaItemInline]
    def album_name(self, obj):
        return obj.album_name

    def album_description(self, obj):
        return obj.album_description
    
    def cover_photo(self, obj):
        return obj.cover_photo
    
    def media_ids(self, obj):
        return obj.media_ids
    
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'chair':
    #         kwargs['queryset'] = Chair.objects.all()  # Replace YourChairModel with the actual Chair model
    #         kwargs['name'] = 'name'  # Replace 'name' with the actual field representing the chair name
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

class MiscAdmin(admin.ModelAdmin):
    list_display = ('Key', 'Value')
    search_fields = ('Key','Value')

    def Key(self, obj):
        return obj.Key
    def Value(self, obj):
        return obj.Value
    
class ScheduleEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_title', 'date', 'start_time', 'end_time')
    search_fields = ('event_title','date', 'start_time', 'end_time')


admin.site.register(Board, BoardAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Chair, ChairAdmin)
admin.site.register(Pager, PagerAdmin) 
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Misc, MiscAdmin)
admin.site.register(Album, GalleryAdmin)
admin.site.register(ScheduleEntry, ScheduleEntryAdmin)