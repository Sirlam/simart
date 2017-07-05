from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'stations/$', views.StationListView.as_view(), name='stations'),
]
