from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^customer/(?P<pk>[0-9]+)/repayment_details/$',
        views.RepaymentDetails.as_view()),
    url(r'^customer/(?P<pk>[0-9]+)/repayment_schedule/$',
        views.RepaymentSchedule.as_view()),
    url(r'^customer/(?P<pk>[0-9]+)/transaction_history/$',
        views.TransactionHistoryDetails.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
