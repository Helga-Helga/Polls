from django.conf.urls import url

from . import views
#from polls.views import DetailView, ResultsView, IndexView

urlpatterns = [
        """
    url(r'^/?$', IndexView.as_view()),
    url(r'^(?P<slug>\d+)/$', DetailView.as_view()),
    url(r'^(?P<question_id>\d+)/results/$', ResultsView.as_view()),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote),
    """,
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # the 'name' value was called by the {% url %} template tag
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls//vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]