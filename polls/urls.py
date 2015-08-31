from django.conf.urls import url

from . import views
#from polls.views import DetailView, ResultsView, IndexView

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # the 'name' value was called by the {% url %} template tag
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls//vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]