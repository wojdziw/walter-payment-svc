from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^waiterapp', hello.views.waiterapp, name='waiterapp'),
    url(r'^postTransactionstatus', hello.views.postTransactionstatus, name='postTransactionstatus'),
    url(r'^getTransactionstatus', hello.views.getTransactionstatus, name='getTransactionstatus'),
    url(r'^getPaymentUri', hello.views.getPaymentUri, name='getPaymentUri'),
    url(r'^getMenuPositions', hello.views.getMenuPositions, name='getMenuPositions'),
    url(r'^admin/', include(admin.site.urls)),
]
