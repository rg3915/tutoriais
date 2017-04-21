from django.conf.urls import url
from myproject.core import views as c

urlpatterns = [
    url(r'^$', c.home, name='home'),
    url(r'^movie/$', c.MovieList.as_view(), name='movie_list'),
    url(r'^movie/(?P<pk>\d+)/$', c.MovieDetail.as_view(), name='movie_detail'),
    url(r'^movie/add/$', c.MovieCreate.as_view(), name='movie_add'),
]
