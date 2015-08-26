from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^(?P<question_id>\d+)/$', views.detail),
    url(r'^(?P<question_id>\d+)/results/$', views.results),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote)

]