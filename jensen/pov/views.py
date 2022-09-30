from django.shortcuts import render
from django.views.generic import ListView
from django_filters.views import FilterView
from pov.models import Album
from pov.filters import AlbumFilter

class PovListView(ListView):
    model = Album
    template_name = 'pov_list.html'

class SearchResultsListView(FilterView):
    model = Album
    context_object_name = 'album_list'
    template_name = 'pov_list.html'
    filterset_class = AlbumFilter 
