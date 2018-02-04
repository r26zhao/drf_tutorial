from django.conf.urls import url
from snippets import views

app_name = 'snippets'

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>\d+)/$', views.snippet_detail),
]