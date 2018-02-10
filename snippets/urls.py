from django.conf.urls import url
from snippets import views

app_name = 'snippets'

urlpatterns = [
    url(r'^snippets/$', views.SnippetsList.as_view()),
    url(r'^snippets/(?P<pk>\d+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),
]