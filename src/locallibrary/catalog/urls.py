from django.conf.urls import url
from .catalog_views.search import Search

urlpatterns = [
    url(r'^videos/?$', Search.as_view(), name='search_video'),
]
