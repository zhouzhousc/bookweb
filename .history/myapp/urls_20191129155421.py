from django.conf.urls import url, includeimport views

urlpatterns = [url(r'add_book$', views.add_book, ),url(r'show_books$', views.show_books, ),]