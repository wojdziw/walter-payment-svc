from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import waiterappbackend.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', waiterappbackend.views.index, name='index'),
    url(r'^waiterapp', waiterappbackend.views.waiterapp, name='waiterapp'),
    url(r'^postTransactionstatus', waiterappbackend.views.postTransactionstatus, name='postTransactionstatus'),
    url(r'^getTransactionstatus', waiterappbackend.views.getTransactionstatus, name='getTransactionstatus'),
    url(r'^getPaymentUri', waiterappbackend.views.getPaymentUri, name='getPaymentUri'),
    url(r'^getMenuPositions', waiterappbackend.views.getMenuPositions, name='getMenuPositions'),
    url(r'^admin/', include(admin.site.urls)),
]
