from django.conf.urls import url,include
from django.contrib import admin
from blog import views

urlpatterns = [

 
        url(r'(?P<id>\d+)/post_edit/$', views.post_edit, name="post_edit"),
    url(r'(?P<id>\d+)/post_delete/$', views.post_delete, name="post_delete"),
    url(r'(?P<id>\d+)/favourite_post/$', views.favorite_post, name="favorite_post"),
    url(r'(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.post_detail, name="post_detail"),
    url(r'post_create/$', views.post_create, name="post_create"),
    url(r'edit_profile/$', views.edit_profile, name="edit_profile"),
     url(r'favorites/$', views.post_favorite_list, name="post_favorite_list"),
       url(r'favorites/$', views.post_favorite_list, name="post_favorite_list"),
      url(r'contact/$', views.contact, name="contact"),
   url(r'users/$', views.usersprofile, name="usersprofile"),






]
