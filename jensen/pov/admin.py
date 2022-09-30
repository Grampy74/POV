from django.contrib import admin
from pov.models import Album, Artist

class AlbumAdmin(admin.ModelAdmin):
    pass
admin.site.register(Album, AlbumAdmin)

class ArtistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Artist, ArtistAdmin)
