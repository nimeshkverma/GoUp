from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/', include('loan_product.v1.urls', namespace='v1')),
]
