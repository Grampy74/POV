from django.urls import path
from pov.views import SearchResultsListView
from pov.filters import AlbumFilter

urlpatterns = [
    path('pov/', SearchResultsListView.as_view(), name='album_list'),
]