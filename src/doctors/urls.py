from django.conf.urls import url
from django.contrib import admin

from .views import (
	doctor_list,
	doctor_create,
	doctor_detail,
	doctor_update,
	doctor_delete,

	patient_create,
	patient_detail,
	patient_update,
	doctors_selection,
	doctor_choose,
	patient_register,
	patient_cancel,
	)


urlpatterns = [
    url(r'^doctor/$', doctor_list, name='list'),
    url(r'^doctor/create/$', doctor_create),
    url(r'^doctor/(?P<id>\d+)/$', doctor_detail, name='detail'),
    url(r'^doctor/(?P<id>\d+)/edit/$', doctor_update, name='update'),
    url(r'^doctor/(?P<id>\d+)/delete/$', doctor_delete),
    url(r'^doctor/(?P<id>\d+)/cancel/$', patient_cancel, name='cancel'),
    url(r'^doctor/(?P<id>\d+)/register/$', patient_register, name='register'),


    url(r'^patient/$', patient_create, name='home'),
    url(r'^patient/(?P<id>\d+)/$', patient_detail, name='detail'),
	url(r'^patient/(?P<id>\d+)/edit/$', patient_update, name='edit'),
    url(r'^patient/(?P<id>\d+)/select/$', doctors_selection, name='select'),
    url(r'^patient/(?P<id>\d+)/select/choice/$', doctor_choose, name='choice'),

]  