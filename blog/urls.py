from django.conf.urls import include, url
from django.contrib import admin
from views import index,show,edit,editAction
urlpatterns = [
    # Examples:
    # url(r'^$', 'boke.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/',index ),
    url(r'^show/(?P<id>[0-9]+)',show,name='show'),
    url(r'^edit/(?P<id>[0-9]+)',edit,name='edit'),
    url(r'^editAction/',editAction,name='editAction')
]
