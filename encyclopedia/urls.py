from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("query", views.query, name="query"), 
    path("new_page", views.new_page, name="new_page"), 
    path("save_entry", views.save_entry, name="save_entry"), 
    path("<str:name>", views.entry, name="entry")
]
