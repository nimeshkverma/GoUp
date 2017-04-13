from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^customer/aadhaar/$', views.AadhaarCreate.as_view(), name='AadhaarCreate'),
    url(r'^customer/(?P<pk>[0-9]+)/aadhaar/$',
        views.AadhaarDetail.as_view(), name='AadhaarDetail'),
    url(r'^customer/(?P<pk>[0-9]+)/aadhaar_otp/$',
        views.AadhaarOTP.as_view(), name='AadhaarOTP'),
    url(r'^customer/(?P<pk>[0-9]+)/aadhaar_ekyc/$',
        views.AadhaarEKYC.as_view(), name='AadhaarEKYC'),
    url(r'^customer/(?P<pk>[0-9]+)/aadhaar_esign/$',
        views.AadhaarESign.as_view(), name='AadhaarESign'),
    url(r'^customer/(?P<pk>[0-9]+)/loan_agreement/$',
        views.LoanAgreement.as_view(), name='LoanAgreement'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
