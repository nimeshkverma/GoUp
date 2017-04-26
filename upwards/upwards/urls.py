from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('aadhaar.urls')),
    url(r'^', include('activity.urls')),
    url(r'^', include('analytics.urls')),
    url(r'^', include('common.urls')),
    url(r'^', include('customer.urls')),
    url(r'^', include('documents.urls')),
    url(r'^', include('eligibility.urls')),
    url(r'^', include('loan_product.urls')),
    url(r'^', include('messenger.urls')),
    url(r'^', include('participant.urls')),
    url(r'^', include('pan.urls')),
    url(r'^', include('social.urls')),
    url(r'^', include('transaction.urls')),
    url(r'^', include('thirdpartyleads.urls')),
    # url(r'^', include('loan.urls')),
]
