from django.conf.urls import patterns, include, url
from bookstore import views

#patron -vista que lo atiende-nombre
urlpatterns = patterns('bookstore.views',
                       url(r'^principal/',"mainPage",name="index"),
                       url(r'^admnistration/',"adminPage",name="administrator"),
                       url()
                      
                      
                      
)