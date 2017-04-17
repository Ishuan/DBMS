from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name="start"),
    url(r'^home', views.home, name='home'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^bio', views.bio, name='bio'),
    url(r'^CS', views.cs, name='cs'),
    url(r'^SIS', views.sis, name='sis'),
    url(r'^fac_bio', views.fac_bio, name='fac_bio'),
    url(r'^fyear_bio', views.fyear_bio, name='fyear'),
    url(r'^fac_cs', views.fac_cs, name='fac'),
    url(r'^fyear_cs', views.fyear_cs, name='fyear'),
    url(r'^fac_sis', views.fac_sis, name='fac'),
    url(r'^fyear_sis', views.fyear_sis, name='fyear'),
    url(r'^course_sis', views.course_sis, name='course_sis'),
    url(r'^getCourseID', views.getCourseID, name='getCourseID'),
    url(r'^getCourseClass', views.getCourseClass, name='getCourseClass'),
    url(r'^getCID', views.getCID, name='getCID'),
    url(r'^office_details', views.office_details, name='office_details'),
    url(r'^year_details', views.year_details, name='year_details'),
]
