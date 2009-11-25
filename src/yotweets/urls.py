from django.conf import settings
from django.conf.urls.defaults import *

handler404 = 'perfect404.views.page_not_found'

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^tasks/', include('tasks.urls')),
        (r'^admin/templatesadmin/', include('templatesadmin.urls')),	
	#(r'^mu/', include('muaccounts.urls')),
	#(r'^create/$', 'muaccounts.views.create_account'),
	
	('^s/', include('shorturls.urls')),
	
	(r'^prepaid/', include('prepaid.urls')),
	(r'^twitter/', include('twitter_app.urls')),
	
	(r'^logout/$', 'django.contrib.auth.views.logout'),
	(r'^admin/', include(admin.site.urls)),
	
	(r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
)

# serve static files in dev mode
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
