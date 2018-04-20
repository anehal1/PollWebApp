from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #127.0.0.1/polls/
    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name="detail"),
    #127.0.0.1/polls/1,2(id )
    url(r'^(?P<question_id>[0-9]+)/result$',views.result, name="result"),
    #127.0.0.1/polls/1,2(id )/result
    url(r'^(?P<question_id>[0-9]+)/vote$',views.vote, name="vote")
    #127.0.0.1/polls/1,2(id )/vote
]