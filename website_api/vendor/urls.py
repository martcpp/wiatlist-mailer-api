from django.urls import path
from .views import vendordetailsView, vendordetailsCreateView


urlpatterns = [
    path('vendordetails/', vendordetailsView.as_view(), name='vendordetails-list'),
    path('vendordetails/create/', vendordetailsCreateView.as_view(), name='vendordetails-create'),
]