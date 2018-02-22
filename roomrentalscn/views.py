from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.http import Http404

from .models import RoomRentalCn

from datetime import date, timedelta, datetime

from django.views.generic.dates import DayArchiveView
    


'''
#note to self:
	remove homeview and replace all Homeview to DayView
'''

class ChineseHomeView(DayArchiveView):

	make_object_list = True 
	allow_future = True
	date_field = "appointmentdate"

	def my_view(request):
		my_objects = list(RoomRentalCn.objects.filter(public=True))
		if not my_objects:
			raise Http404("No MyModel matches the given query.")


	def get(self, request, *args, **kwargs):

		todaydate 		= date.today()
		tomorrowdate 	= todaydate + timedelta(days=1)
		tmonth 			= tomorrowdate.strftime('%b')
		tday 			= tomorrowdate.strftime('%d')
		tyear 			= tomorrowdate.strftime('%Y')

		yesterdaydate 	= todaydate - timedelta(days=1) 
		ymonth 			= yesterdaydate.strftime('%b')
		yday 			= yesterdaydate.strftime('%d')
		yyear 			= yesterdaydate.strftime('%Y')

		

		user = self.request.user

		qs = RoomRentalCn.objects.filter(user__is_active=True, appointmentdate=todaydate).order_by("appointmenttime")
#		if todaydate = 
		return render(request, "roomrentalscn/chi-home-feed.html", {'object_list':qs, 'previous':False, 'today':todaydate, 
			'tyear':tyear, 'tmonth':tmonth, 'tday':tday, 'yyear':yyear, 'ymonth':ymonth, 'yday':yday})


class ChineseDayView(DayArchiveView):


	def my_view(request):
		my_objects = list(RoomRentalCn.objects.filter(public=True))
		if not my_objects:
			raise Http404("No MyModel matches the given query.")


	def get_queryset(self, *args, **kwargs):
		#if user is not authenticated
		return RoomRentalCn.objects.filter(user__is_active=True)

	date_field = "appointmentdate" 
	make_object_list = True 
	allow_future = True
	allow_empty = True

	def get_context_data(self, *args, **kwargs):

		year 			= self.kwargs['year']
		month 			= self.kwargs['month']
		day				= self.kwargs['day']

		q_date			= datetime.strptime(month + day + year, '%b%d%Y')
		tomorrowdate 	= q_date + timedelta(days=1)
		tmonth 			= tomorrowdate.strftime('%b')
		tday 			= tomorrowdate.strftime('%d')
		tyear			= tomorrowdate.strftime('%Y')

		yesterdaydate 	= q_date - timedelta(days=1) 
		ymonth 			= yesterdaydate.strftime('%b')
		yday 			= yesterdaydate.strftime('%d') 
		yyear			= yesterdaydate.strftime('%Y')

	
		#print(RoomRental.objects.filter(appointmentdate=tomorrowdate)[1])

		
		context = super(DayArchiveView, self).get_context_data(*args, **kwargs)

		context['tmonth'] 	= tmonth
		context['tday'] 	= tday
		context['tyear'] 	= tyear
		context['ymonth'] 	= ymonth
		context['yday'] 	= yday
		context['yyear'] 	= yyear
		context['cdate']	= q_date


		todaysdate 		= date.today()
		secsfromtoday	= (todaysdate - q_date.date()).total_seconds()
		print(secsfromtoday)

		# if it is 3 days later, no more next button
		if secsfromtoday == -259200:
			context['next'] = False

		# if it is Today, no more previous button
		if secsfromtoday == 0:
			context['previous'] = False

		# if it is 3+ days later, no more previous and next button
		if secsfromtoday < -259200:
			context['next'] = False
			context['previous'] = False

		# if it is past today, no more previous and next button
		if secsfromtoday > 0:
			context['previous'] = False
			context['next'] = False


		return context




'''Create and update: 


class RoomRentalCreateView(CreateView, LoginRequiredMixin):
	template_name = 'form.html'
	form_class = RoomRentalForm

	def form_valid(self, form):		
		obj = form.save(commit=False)
		obj.user = self.request.user
		return super(RoomRentalCreateView, self).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super(RoomRentalCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def get_queryset(self):
		#if user is authenticated
		return RoomRental.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(RoomRentalCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Create RoomRental'
		return context

class RoomRentalUpdateView(UpdateView, LoginRequiredMixin):
	template_name 	= 'roomrentals/detail-update.html'
	form_class = RoomRentalForm
	
	def get_queryset(self):
		#if user is authenticated
		return RoomRental.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(RoomRentalUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update RoomRental'
		return context

	def get_form_kwargs(self):
		kwargs = super(RoomRentalUpdateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs
'''

'''
HOMEVIEW IN 2017!

class HomeView(View):

	make_object_list = True 
	allow_future = True
	date_field = "appointmentdate"


	def get(self, request, *args, **kwargs):
		todaydate = date.today()
		
		tomorrowdate 	= todaydate + timedelta(days=1)
		tmonth 			= tomorrowdate.strftime('%b')
		tday 			= tomorrowdate.strftime('%d')
		tyear 			= tomorrowdate.strftime('%Y')

		yesterdaydate 	= todaydate - timedelta(days=1) 
		ymonth 			= yesterdaydate.strftime('%b')
		yday 			= yesterdaydate.strftime('%d')
		yyear 			= yesterdaydate.strftime('%Y')

		if not request.user.is_authenticated():
			object_list = RoomRental.objects.filter(public=True, appointmentdate=todaydate).order_by('appointmentdate')
			return render(request, "home.html", {"object_list": object_list,'today':todaydate, 
			'tyear':tyear, 'tmonth':tmonth, 'tday':tday, 'yyear':yyear,'ymonth':ymonth, 'yday':yday})

		#if not request.user.is_authenticated():
		#	return render(request, "home.html", {})

		user = self.request.user
		#is_following_user_ids = [x.user.id for x in user.is_following.all()]
		#qs = RoomRental.objects.filter(user__id__in=is_following_user_ids, public=True).order_by("-updated")[:4]
		qs = RoomRental.objects.filter(user=user, appointmentdate=todaydate).order_by("appointmenttime")
#		if todaydate = 
		return render(request, "roomrentals/home-feed.html", {'object_list':qs, 'title':todaydate, 'today':todaydate, 
			'tyear':tyear, 'tmonth':tmonth, 'tday':tday, 'yyear':yyear, 'ymonth':ymonth, 'yday':yday})
'''



