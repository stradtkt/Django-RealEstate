from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name="listings"),
    url(r'^(?P<id>\d+)/$', views.listing, name="listing"),
    path('search', views.search, name="search")
]