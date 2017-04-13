from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^customer/loan_product/$',
        views.LoanProductCreate.as_view(), name='LoanProductCreate'),
    url(r'^customer/(?P<pk>[0-9]+)/loan_product/$',
        views.LoanProductDetail.as_view(), name='LoanProductDetail'),
    url(r'^customer/(?P<pk>[0-9]+)/loan_specifications/$',
        views.LoanSpecifications.as_view(), name='LoanSpecifications'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
