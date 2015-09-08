from django.conf.urls import include, url
# from Django 1.8.1
#from django.conf.urls import patterns, include, url

from django.contrib import admin
# from Django 1.8.1
# admin.autodiscover()
# import hello.views
#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'^$', hello.views.index, name='index'),
#    url(r'^db', hello.views.db, name='db'),
#    url(r'^admin/', include(admin.site.urls)),

urlpatterns = [
    url(r'^$', include('hello.urls')),
    url(r'^db', include('hello.urls')),
    url(r'^hello/', include('hello.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls))
    ]
