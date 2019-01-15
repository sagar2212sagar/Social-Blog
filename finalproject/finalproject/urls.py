from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

#urlpatterns = [
 #   url(r'^admin/', admin.site.urls),
  #  url(r'^$',views.user_login,name='user_login'),

   # url(r'^blog/',include('blog.urls',namespace='blog')),
   # url(r'^post/$',views.post_list,name='post_list'),
   # url(r'^logout/$',views.user_logout,name='user_logout'),

    #url(r'^password-reset/$', auth_views.password_reset, name="password_reset"),
     #url(r'^password-reset/done/$', auth_views.password_reset_done, name="password_reset_done"),
     #url(r'^password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/$', auth_views.password_reset_confirm, name="password_reset_confirm"),
     #url(r'^password-reset/complete/$', auth_views.password_reset_complete, name="password_reset_complete"),
    #url(r'^register/$',views.register,name='register'),
     #url(r'^user/',views.usersprofile,name='usersprofile'),
    #url(r'^like/',views.like_post,name='like_post'),


urlpatterns = [

     url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name="post_list"),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^login/$', views.user_login, name="user_login"),
     url(r'^contact/$', views.contact, name="contact"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^register/$', views.register, name="register"),

    # Password Reset Url's
    # url(r'^password-reset/$', auth_views.password_reset, name="password_reset"),
    # url(r'^password-reset/done/$', auth_views.password_reset_done, name="password_reset_done"),
    # url(r'^password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/$', auth_views.password_reset_confirm, name="password_reset_confirm"),
    # url(r'^password-reset/complete/$', auth_views.password_reset_complete, name="password_reset_complete"),

  #  url(r'^', include('django.contrib.auth.urls')),
   # url(r'^oauth/', include('social_django.urls', namespace="social")),
    url(r'^like/', views.like_post, name="like_post"),





]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
