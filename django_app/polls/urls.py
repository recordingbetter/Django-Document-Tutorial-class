from django.conf.urls import url

from . import views

# from polls import views

urlpatterns = [
    url(r'^$', views.index, name = 'index')
]
