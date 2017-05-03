from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^analytics/algo360/$', views.Algo360DataDetails.as_view(),
        name='Algo360DataDetails'),
    url(r'^analytics/customer/(?P<pk>[0-9]+)/credit_report/$',
        views.CreditReportDetails.as_view(), name='CreditReportDetails'),
    url(r'^customer/datalog/$', views.DataLogCreate.as_view(), name='DataLogCreate'),
    url(r'^customer/(?P<pk>[0-9]+)/datalog/$',
        views.DataLogDetail.as_view(), name='DataLogDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
