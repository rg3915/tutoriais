from django.conf.urls import url
from .views import home, movie_list


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^movie/$', movie_list, name='movie_list'),
]
