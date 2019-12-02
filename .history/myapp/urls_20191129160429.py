from django.conf.urls import url, include
import myapp.views

urlpatterns = [url(r'add_book$', views.add_book, ),url(r'show_books$', views.show_books, ),]