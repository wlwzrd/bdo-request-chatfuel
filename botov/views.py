from django.shortcuts import render
from django.http import HttpResponse
from math import pow
from datetime import datetime
import pytz
import json

# Create your views here.

def index(request):
	return HttpResponse("JulietaLabs's API services for BOT")

def getCarFee(request):
	amount = int(request.GET.get("veh_amount"))
	rate = float(request.GET.get("veh_rate"))
	term = int(request.GET.get("veh_term"))
	seg = int(request.GET.get("seg_rate"))
	json_data= {}
	data = {}
	insurance = (seg * amount)/1000000
	rate = rate/100
	upper = rate*pow((1+rate),term)
	lower = pow((1+rate),term)-1
	fee = amount * (upper/lower)
	data ["veh_fee"] = "${:,.0f}".format(fee+insurance).replace(',','.')
	json_data["set_attributes"]=data
	return HttpResponse(json.dumps(json_data,indent=4), content_type="application/json")

def getCurrentTime(request):
	tz = pytz.timezone('America/Bogota')
        today = datetime.now(tz)
        day =  today.weekday()
        hour =  today.hour
        json_data = {}
        data = {}
        data ["day"] = int(day)
        #data ["day"] =  0
        #data ["hour"] = 8
        data ["hour"] = int(hour)
        json_data ["set_attributes"] =  data
        return HttpResponse(json.dumps(json_data, indent=4), content_type="application/json")


