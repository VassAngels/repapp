from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'index2',views.index2),
    url(r'explore',views.explore)
]
