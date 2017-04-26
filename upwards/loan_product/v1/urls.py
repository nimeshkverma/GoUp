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
    url(r'^customer/(?P<pk>[0-9]+)/loan_agreement/$',
        views.LoanAgreement.as_view(), name='LoanAgreement'),
    url(r'^customer/(?P<pk>[0-9]+)/loan_disbursal_details/$',
        views.LoanDisbursalDetails.as_view(), name='LoanDisbursalDetails'),
    url(r'^customer/(?P<pk>[0-9]+)/new_loan/$',
        views.NewLoanDetails.as_view(), name='NewLoanDetails'),
    url(r'^loan_product/bike_worth/$',
        views.BikeWorthDetails.as_view(), name='BikeWorthDetails'),
    url(r'^customer/loan_product/bike_loan/$',
        views.BikeLoanCreate.as_view(), name='BikeLoanCreate'),
    url(r'^customer/(?P<pk>[0-9]+)/loan_product/bike_loan/$',
        views.BikeLoanDetail.as_view(), name='BikeLoanDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
