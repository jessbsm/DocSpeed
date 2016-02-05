from django.contrib import admin

# Register your models here.
from .models import Doctor, Patient

class DoctorModelAdmin(admin.ModelAdmin):
	list_display = ["__str__","speciality","phone", "id"]
	list_filter = ["name","speciality"]
	search_fields =["speciality","schedule"]
	class Meta:
		model = Doctor

admin.site.register(Doctor, DoctorModelAdmin)


class PatientModelAdmin(admin.ModelAdmin):
	list_display = ["__str__", "id"]
	search_fields =["name"]
	class Meta:
		model = Patient

admin.site.register(Patient, PatientModelAdmin)