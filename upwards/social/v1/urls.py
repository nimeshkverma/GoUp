from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^customer/social_login/$',
        views.SocialLogin.as_view(), name='SocialLogin'),
    url(r'^customer/(?P<pk>[0-9]+)/social_logout/$',
        views.SocialLogout.as_view(), name='SocialLogout'),
    url(r'^customer/linkedin_auth$',
        views.LinkedinAuth.as_view(), name='LinkedinAuth'),
    url(r'^customer/(?P<customer_id>[0-9]+)/social_profiles/$',
        views.SocialProfiles.as_view(), name='SocialProfiles')

]

urlpatterns = format_suffix_patterns(urlpatterns)
