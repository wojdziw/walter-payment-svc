from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import waiterappbackend.views

urlpatterns = [
    url(r'^$', waiterappbackend.views.index, name='index'),
    url(r'^waiterapp', waiterappbackend.views.waiterapp, name='waiterapp'),
    url(r'^postTransactionStatus', waiterappbackend.views.postTransactionStatus, name='postTransactionStatus'),
    url(r'^getTransactionStatus', waiterappbackend.views.getTransactionStatus, name='getTransactionStatus'),
    url(r'^getPaymentUri', waiterappbackend.views.getPaymentUri, name='getPaymentUri'),
    url(r'^getMenuPositions', waiterappbackend.views.getMenuPositions, name='getMenuPositions'),
    url(r'^admin/', include(admin.site.urls)),
]
