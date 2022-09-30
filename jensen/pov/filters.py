from pov.models import Album
import django_filters


class AlbumFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Album
        fields = ['artist_name', 'album_name']