from django.shortcuts import render
from django.http import HttpResponse
from math import pow
import json

# Create your views here.

def index(request):
	return HttpResponse("Banco de Occidente's BOT for Virtual Office")

def getCarFee(request):
	amount = int(request.GET.get("veh_amount"))
	rate = float(request.GET.get("veh_rate"))
	term = int(request.GET.get("veh_term"))
	json_data= {}
	data = {}
	rate = rate/100
	upper = rate*pow((1+rate),term)
	lower = pow((1+rate),term)-1
	fee = amount * (upper/lower)
	data ["veh_fee"] = "${:,.0f}".format(fee)
	json_data["set_attributes"]=data
	return HttpResponse(json.dumps(json_data,indent=4), content_type="application/json")
