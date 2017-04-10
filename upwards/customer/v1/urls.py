from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^customer/personal/$', views.CustomerList.as_view(),
        name='CustomerList'),
    url(r'^customer/(?P<pk>[0-9]+)/personal/$',
        views.CustomerDetail.as_view(), name='CustomerDetail'),
    url(r'^customer/bank/$', views.BankDetailsCreate.as_view(),
        name='BankDetailsCreate'),
    url(r'^customer/(?P<pk>[0-9]+)/bank/$',
        views.BankDetails.as_view(), name='BankDetails'),
    url(r'^customer/(?P<pk>[0-9]+)/homepage/$',
        views.HomepageAPI.as_view(), name='HomepageAPI'),
    url(r'^customer/(?P<customer_id>[0-9]+)/clear_all_customer_data/$',
        views.ClearAllCustomerData.as_view(), name='ClearAllCustomerData'),
]
