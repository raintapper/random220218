from django.conf import settings
from django.urls import reverse
from django.db import models

User = settings.AUTH_USER_MODEL
class RoomRentalCn(models.Model):

	# associations
	user 			= models.ForeignKey(User, on_delete=models.CASCADE)
	# item stuff
	streetname		= models.CharField(max_length=120, null=True, blank=True)
	postalcode		= models.CharField(max_length=120, null=True, blank=True)
	block	 		= models.CharField(max_length=120, null=True, blank=True) 
	roomtype 		= models.CharField(max_length=120, null=True, blank=True) 
	price 			= models.CharField(max_length=120, null=True, blank=True) 
	public 			= models.BooleanField(default=True)
	appointmentdate	= models.DateField(max_length=120, null=True, blank=True)
	appointmenttime = models.TimeField(max_length=120, null=True, blank=True)
	#image_url (Add Image to be discussed later)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)

	def __str__(self):

		address = str(self.streetname) + " " + str(self.block)

		return address

	def get_absolute_url(self):
		return reverse('roomrentalscn:detail', kwargs= {'pk': self.pk})


	class Meta:
		#reverse updated, reverse timestamp. 
		#get the most recently updated first that is why the '-' sign
		ordering = ['-updated', 'timestamp']

'''
	# if 
	def get_itemdesc(self):
		return self.itemdesc.split(",")

	def get_itemnote(self):
		return self.itemnote.split(",")
'''




