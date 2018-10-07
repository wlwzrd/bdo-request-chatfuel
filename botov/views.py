from django.shortcuts import render
from django.http import HttpResponse
from math import pow
import json

# Create your views here.

def index(request):
	return HttpResponse("JulietaLabs's API services for BOT")

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

def getReceipt(request):
	product_quantity = int(request.GET.get("product_quantity"))
	beer_price = 2700
	json_data = {}
	messages = []
	attachment = {}
	payload = {}
	address = {}
	summary = {}
	elements = []
	payload["template_type"] = "receipt"
	payload["recipient_name"] = "Mario Gutierrez"
	payload["order_number"] = "12345678901"
	payload["currency"] = "COP"
	payload["payment_method"] = "Efectivo"
	payload["order_url"] = "www.instagram.com/wlwzrd"
	payload["timestamp"] = "1428444666"
	address["street_1"] = "AV 2HN No 54N-05, Apto 503C"
	address["street_2"] = ""
	address["city"] = "Cali"
	address["postal_code"] = "760001"
	address["state"] = "VA"
	address["country"] = "CO"
	payload["address"] =  address
	summary["subtotal"] = product_quantity * beer_price
	summary["shipping_cost"] = 3500
	summary["total_tax"] = 1500
	summary["total_cost"] = (product_quantity * beer_price)+ 3500 +1500 -2500
	payload["summary"] = summary
	payload["adjustments"] = [{"name":"Descuento ", "amount":-2500}]
	elements.append({"title":"Cerveza Poker", "subtitle":"300ml", "quantity":product_quantity, "price":beer_price, "currency":"COP", "image_url":"https://d50xhnwqnrbqk.cloudfront.net/images/products/large/Poker.jpg"})
	payload["elements"] = elements
	attachment["type"] = "template"
	attachment["payload"] = payload
	messages.append({"attachment":attachment})
	json_data["messages"] = messages
	return HttpResponse(json.dumps(json_data, indent=4),content_type="application/json")
