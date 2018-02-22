
from django.urls import re_path, include, path
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, LogoutView

from roomrentals.views import HomeView
from roomrentalscn.views import ChineseHomeView

urlpatterns = [
	path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='ENG_home'),
    path('cn/', ChineseHomeView.as_view(), name='CHI_home'),
    path('roomrentals/', include('roomrentals.urls', namespace='roomrentals')),
    path('roomrentalscn/', include('roomrentalscn.urls', namespace='roomrentalscn')),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('aboutcn/', TemplateView.as_view(template_name='aboutcn.html'), name='aboutcn'),
    path('contact/',  TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('contactcn/',  TemplateView.as_view(template_name='contactcn.html'), name='contactcn'),
]
