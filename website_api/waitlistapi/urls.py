from django.urls import path
from .views import WaitlistEntryView , Waitlist



urlpatterns = [
    path('waitlist/', WaitlistEntryView.as_view(), name='waitlist-entry'),
    path('wait/', Waitlist.as_view(), name='waitlist-list'),
]
