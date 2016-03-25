from django.contrib import admin
from main.models import HouseHold, Individual, LastName, Notes

# Register your models here.

class HouseHoldAdmin(admin.ModelAdmin):
	list_display = ("address",)
	search_fields = ["address"]
	
	
class LastNameAdmin(admin.ModelAdmin):
	list_display = ("last_name",)
	search_field = ["last_name"]


class IndividualAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "age", "sex", "family_role", "member_status", )
	search_fields = ["first_name", "last_name", "age", "sex", "family_role", "member_status"]


class NotesAdmin(admin.ModelAdmin):
	list_display = ("last_name", "date_posted")

admin.site.register(HouseHold, HouseHoldAdmin)
admin.site.register(Individual, IndividualAdmin)
admin.site.register(LastName, LastNameAdmin)
admin.site.register(Notes, NotesAdmin)