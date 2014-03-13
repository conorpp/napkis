from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('napkis.apps.menu.views',
    url(r'^test/$', 'test'),
    url(r'^testing/$', 'testing'),
    url(r'^add/menuitem/$', 'addMenuItem'),
    url(r'^get/menuitem/$', 'getMenuItems'),
    url(r'^menu/$', 'menu'),
    url(r'^$', 'index'),
)
