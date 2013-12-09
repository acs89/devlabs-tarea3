from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from devLabs_tarea3 import views, settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^admin/', include(admin.site.urls)),
   url(r'^$', views.index, name='home'),
   url(r'^search/$', views.search),
   url(r'^exito/$', views.exito),
   url(r'^fail/$', views.fail),
) 

urlpatterns += staticfiles_urlpatterns()
