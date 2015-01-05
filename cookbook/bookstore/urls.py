from django.conf.urls import patterns, include, url
from bookstore import views

#patron -vista que lo atiende-nombre
urlpatterns = patterns('bookstore.views',
                       #main page
                       url(r'^principal/',"mainPage",name="index"),
                       
                       #listing views
                       url(r'^bookcatalog',"listBooks",name="catalog"),
                       url(r'^authorList',"listAuthors",name="authors"),
                       url(r'^editorList',"listEditors",name="editors"),
                       url(r'^categories',"listCategories",name="categories"),
                       
                       
                       url(r'^admnistration/',"adminPage",name="administrator"),
                      
                      
                      
)