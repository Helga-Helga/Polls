from django.conf.urls import url

from . import views
from polls.views import DetailView, ResultsView, IndexView

urlpatterns = [

    url(r'^/?$', IndexView.as_view),
    url(r'^(?P<question_id>\d+)/$', DetailView.as_view),
    url(r'^(?P<question_id>\d+)/results/$', ResultsView.as_view),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote)

]