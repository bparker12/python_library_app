from django.conf.urls import url, include
from .views import *


app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^book/form$', book_form, name='book_form'),
    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^libraries$', library_list, name='libraries'),
    url(r'^library/form$', library_form, name='library_form'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
]