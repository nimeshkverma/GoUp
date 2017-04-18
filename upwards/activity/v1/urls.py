from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^customer/(?P<pk>[0-9]+)/state_change/$',
        views.CustomerStateChange.as_view(), name='CustomerStateChange'),
    url(r'^customer/(?P<pk>[0-9]+)/kyc_review_submit/$',
        views.KYCReviewSubmit.as_view(), name='KYCReviewSubmit'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
