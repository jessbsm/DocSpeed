from django import forms


from .models import Doctor, Patient


class DoctorForm(forms.ModelForm):
	class Meta:
		model = Doctor
		fields = [
			"name",
			"speciality",
			"num_street",
			"type_street",
			"name_street",
			"city",
			"phone",
			"schedule"
		]



class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = [
			"name",
			"num_street",
			"type_street",
			"name_street",
			"city",
		]