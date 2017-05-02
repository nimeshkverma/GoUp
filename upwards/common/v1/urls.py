from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^common/config/$', views.Config.as_view(), name='config'),
    url(r'^common/dropdown_data/$',
        views.DropdownData.as_view(), name='dropdown_data'),
    url(r'^common/college/$', views.CollegeList.as_view()),
    url(r'^common/college/(?P<pk>[0-9]+)/$', views.CollegeDetail.as_view()),
    url(r'^common/company/$', views.CompanyList.as_view()),
    url(r'^common/company/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view()),
    url(r'^common/salary_payment_mode/$',
        views.SalaryPaymentModeList.as_view()),
    url(r'^common/salary_payment_mode/(?P<pk>[0-9]+)/$',
        views.SalaryPaymentModeDetail.as_view()),
    url(r'^common/organisation_type/$', views.OrganisationTypeList.as_view()),
    url(r'^common/organisation_type/(?P<pk>[0-9]+)/$',
        views.OrganisationTypeDetail.as_view()),
    url(r'^common/profession_type/$', views.ProfessionTypeList.as_view()),
    url(r'^common/profession_type/(?P<pk>[0-9]+)/$',
        views.ProfessionTypeDetail.as_view()),
    url(r'^common/loan_purpose/$', views.LoanPurposeList.as_view()),
    url(r'^common/loan_purpose/(?P<pk>[0-9]+)/$',
        views.LoanPurposeDetail.as_view()),
    url(r'^common/bike/$', views.BikeList.as_view()),
    url(r'^common/bike/(?P<pk>[0-9]+)/$',
        views.BikeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
