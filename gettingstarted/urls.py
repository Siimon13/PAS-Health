from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import pas.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
        url(r'^$', pas.views.index, name='index'),
    url(r'^render_results/$', pas.views.render_results, name = 'results'),
    url(r'^update_results/$', pas.views.update_results, name = 'update'),
    url(r'^admin/', include(admin.site.urls)),
    ]
