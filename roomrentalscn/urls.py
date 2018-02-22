from django.urls import re_path

from .views import (
    ChineseDayView,
    )

app_name = 'roomrentalscn'

urlpatterns = [
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$',ChineseDayView.as_view(), name='archive_day'),
    #url(r'^create/$', RoomRentalCreateView.as_view(), name='create'),
    #url(r'^(?P<pk>\d+)/edit/$', RoomRentalUpdateView.as_view(), name='edit'),
    #url(r'^(?P<pk>\d+)/$', RoomRentalUpdateView.as_view(), name='detail'),
	
	# dollarsign '$' is end of string
]
