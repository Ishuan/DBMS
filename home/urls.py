from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name="start"),
    url(r'^home', views.home, name='home'),
    url(r'^BIOINFO', views.bio, name='bio'),
    url(r'^CS', views.cs, name='cs'),
    url(r'^SIS', views.sis, name='sis'),
]
