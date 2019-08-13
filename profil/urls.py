from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sejarah$', views.sejarah),
    url(r'^vm$', views.vm),
    url(r'^prestasi$', views.prestasi),
    url(r'^fasil$', views.fasil),
]