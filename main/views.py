from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, DetailView
from main.models import Individual, LastName, HouseHold, Notes


# Create your views here.

#class HouseholdListView(ListView):
#	model = HouseHold
#	template_name = "household.html"
#	context_object_name = "household_list"


def family_info(request):

	lastname = LastName.objects.all()
	print lastname
#	filter(last_name=pk)
	notes = Notes.objects.all()
#	get(pk=pk)
	household = HouseHold.objects.all()
	context={}

	context['lastname'] = lastname
	context['notes'] = notes
	context['household_list'] = household


	return render(request, 'household.html', context)