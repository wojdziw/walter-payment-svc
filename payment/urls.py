from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import payment.views

urlpatterns = [
    url(r'^$', payment.views.index, name='index'),
    url(r'^payment', payment.views.payment, name='payment'),
    url(r'^postTransactionStatus', payment.views.postTransactionStatus, name='postTransactionStatus'),
    url(r'^getTransactionStatus', payment.views.getTransactionStatus, name='getTransactionStatus'),
    url(r'^getPaymentUri', payment.views.getPaymentUri, name='getPaymentUri'),
    url(r'^getMenuPositions', payment.views.getMenuPositions, name='getMenuPositions'),
    url(r'^admin/', include(admin.site.urls)),
]
