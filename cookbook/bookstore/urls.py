from django.conf.urls import patterns, include, url
from bookstore import views

#patron -vista que lo atiende-nombre
urlpatterns = patterns('bookstore.views',
                       #main page
                       url(r'^principal/',"principal",name="principal"),
                       
                       #listing views
                       url(r'^bookcatalog',"listBooks",name="catalog"),
                       url(r'^authorList',"listAuthors",name="authors"),
                       url(r'^editorList',"listEditors",name="editors"),
                       url(r'^categories',"listCategories",name="categories"),
                       
                       #adding views
                       url(r'^addbook',"addBook",name="addBook"),
                       url(r'^addAuthor',"addAuthor",name="addAuthor"),
                       url(r'^addEditor',"addEditor",name="addEditor"),
                       url(r'^addCategory',"addCategory",name="addCategory"),
                       
                       #deleting views
                       url(r'^deleteBook/(?P<pk>\d+)',"deleteBook",name="deleteBook"),
                       url(r'^deleteAuthor/(?P<pk>\d+)',"deleteAuthor",name="deleteAuthor"),
                       url(r'^deleteEditor/(?P<pk>\d+)',"deleteEditor",name="deleteEditor"),
                       url(r'^deleteCategory/(?P<pk>\d+)',"deleteCategory",name="deleteCategory"),
                       
                       #changing views
                       url(r'^changeBook/(?P<pk>\d+)',"changeBook",name="changeBook"),
                       url(r'^changeAuthor/(?P<pk>\d+)',"changeAuthor",name="changeAuthor"),
                       url(r'^changeEditor/(?P<pk>\d+)',"changeEditor",name="changeEditor"),
                       url(r'^changeCategory/(?P<pk>\d+)',"changeCategory",name="changeCategory"),
                       
                       url(r'^admnistration/',"administrator",name="administrator"),
                      
                      
                      
)