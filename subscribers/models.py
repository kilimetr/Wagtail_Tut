from django.db import models

# Create your models here.


class Subscribers(models.Model):
	email = models.CharField(max_length = 100, blank = False, null = False, help_text = "Email Address")
	full_name = models.CharField(max_length = 100, blank = False, null = False, help_text = "First and last name")
	
	def __str__(self):
		# string representation
		return self.full_name

	class Meta:
		verbose_name = "SubscriberssS"
		verbose_name_plural = "SubscriIiberssS"



