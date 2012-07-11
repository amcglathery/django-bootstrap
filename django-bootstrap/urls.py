from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^boards/$', 'boards.views.index'),
    url(r'^boards/(?P<board_id>\d+)/$', 'boards.views.detail'),
    url(r'^games/(?P<game_id>>\d+)/$', 'boards.views.game'),
    url(r'^users/(?P<game_id>\d+)/$', 'boards.views.user'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
            url(r'^static/(?P<path>.*)$', 'serve'),
    )
