from __future__ import unicode_literals

from django.db import models

# Create your models here.


class HouseHold(models.Model):
	address = models.CharField(max_length=100)
	
	def __str__(self):
		return self.address

	
class LastName(models.Model):
	last_name = models.CharField(max_length=25, blank=True)
	household = models.ForeignKey("main.household")
	
	def __str__(self):
		return self.last_name
	
	
class Individual(models.Model):
	first_name = models.CharField(max_length=25, blank=True)
	last_name = models.ForeignKey("main.lastname")
	age = models.IntegerField(null=True, blank=True)
	sex = models.CharField(max_length=1, blank=True)
	family_role = models.CharField(max_length=15, blank=True)
	member_status = models.CharField(max_length=15, blank=True)
	notes_body = models.ForeignKey("main.notes", null=True, blank=True)

def __str__(self):
		return "%s %s Age: %s Sex: %s Family Role: %s Member Status: %s" %(self.first_name, self.last_name, str(self.age), self.sex, self.family_role, self.member_status)
	
	
class Notes(models.Model):
	notes_body = models.TextField()
	date_posted = models.DateField(null=True, blank=True)
	last_name = models.ForeignKey("main.lastname")
	
	def __int__(self):
		return self.date_posted
	def __str__(self):
		return (str(self.last_name))
	class Meta:
		verbose_name_plural = 'notes'