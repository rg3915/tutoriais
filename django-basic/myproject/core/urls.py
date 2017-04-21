from django.conf.urls import url
from .views import home, movie_list, movie_detail


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^movie/$', movie_list, name='movie_list'),
    url(r'^movie/(?P<pk>\d+)/$', movie_detail, name='movie_detail'),
]
