from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookstore import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cookbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookstore/',include('bookstore.urls')),
)
