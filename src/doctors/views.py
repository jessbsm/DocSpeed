from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, redirect

from .forms import DoctorForm, PatientForm
from .models import Doctor, Patient, adress


def doctor_create(request):
	form = DoctorForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		ad=adress(instance.num_street, instance.type_street, instance.name_street, instance.city)
		coord=ad.get_lat_lng()
		latitude=coord[0]
		longitude=coord[1]
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_doctor_url())
	context = {
		"form": form,
	}
	return render(request, "doctor_form.html",context)

def doctor_detail(request, id=None): 
	instance = get_object_or_404(Doctor, id=id)
	queryset = Patient.objects.filter(doctor__pk=instance.id) #)[Patient.objects.filter(doctor__pk=instance.id).count()-1:] #[Patient.objects.all().count()-1] #filter(doctor__pk=instance.id)
	context = {
		"title": instance.name,
		"instance": instance,
		"pat_list": queryset
	}
	return render(request, "doctor_detail.html",context)

def doctor_list(request): 
	queryset=Doctor.objects.all()
	context = {
			"doctors_list": queryset,
			"title": "Liste des médecins"
		}
	return render(request, "doctor_list.html",context)

def doctor_update(request, id=None):
	instance = get_object_or_404(Doctor, id=id)
	form = DoctorForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Changes Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_doctor_url())

	context = {
		"title": instance.name,
		"instance": instance,
		"form": form,
	}
	return render(request, "doctor_update.html",context)


def doctor_delete(request, id=None):
	instance = get_object_or_404(Doctor, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("doctor:list") 




def patient_create(request):
	form = PatientForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		queryset=Doctor.objects.all()
		context = {
			"title": instance.name,
			"instance": instance
		}
		return HttpResponseRedirect(instance.get_patient_url())
	context = {
		"form": form,
	}
	return render(request, "patient_form.html",context)


def patient_detail(request, id=None): 
	instance = get_object_or_404(Patient, id=id)
	context = {
		"title": instance.name,
		"instance": instance
	}
	return render(request, "patient_detail.html",context)


def patient_update(request, id=None):
	instance = get_object_or_404(Patient, id=id)
	form = PatientForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Changes Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_patient_url())

	context = {
		"title": instance.name,
		"instance": instance,
		"form": form,
	}
	return render(request, "patient_update.html",context)


def doctor_choose(request, id=None):
	queryset = Patient.objects.all()
	instance1 = queryset[queryset.count()-1]
	instance1.save()
	instance2 = get_object_or_404(Doctor, id=id)
	instance2.save()
	instance1.doctor = instance2
	instance2.Patient_set.add(instance1)
	context = {
		"title": instance2.name,
		"instance1": instance1,
		"instance2": instance2,
	}
	return render(request, "doctor_choose.html",context)


def doctors_selection(request, id=None): 
	instance = get_object_or_404(Patient, id=id)
	instance.save()
	queryset=Doctor.objects.all()
	context = {
			"doctors_list": queryset,
			"title": "Liste des médecins aux alentours",
			"instance": instance,
		}
	return render(request, "doctors_selection.html",context)


def patient_register(request, id=None):
	instance = get_object_or_404(Doctor, id=id)
	patients = Patient.objects.filter(doctor__pk=instance.id)
	last_patient = patients[patients.count()-1]
	context = {
			"pat": last_patient,
			"doc": instance,
	}
	return render(request, "register.html")


def patient_cancel(request, id=None):
	instance = get_object_or_404(Doctor, id=id)
	patients = Patient.objects.filter(doctor__pk=instance.id)
	cancelor = patients[patients.count()-1]
	return render(request, "cancel.html")
