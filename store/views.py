from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods
from models import Customer, Order, OrderItems
# Create your views here.


#@require_http_methods(["GET"])
def createCustomer(request):
	userMessengerId = request.GET.get("userMessengerId")
	userName = request.GET.get("userName")
	userLastName = request.GET.get("userLastName")
	userPhone = request.GET.get("userPhone")
	userEmail = request.GET.get("userEmail")
	data = {}
	jsonData = {}
	createStatus = False
	createMessage = "ID: " + userMessengerId + " Name: " + userName
	try:
		new_customer = Customer(messenger_user_id=userMessengerId,
					name=userName + " " + userLastName,
					phone=userPhone,
					email=userEmail)
		new_customer.save()
		createStatus = True
		createMessage = "Customer created"
	except ValidationError as ve:
		createStatus = False
		createMessage =  str(ve) 
	except IntegrityError as ie:
		createStatus = False
		createMessage = "User already exist!"
	data["createStatus"] = createStatus
	data["createMesage"] = createMessage
	jsonData["set_attributes"] = data
	return HttpResponse(json.dumps(jsonData, indent=4), content_type="application/json")

def getOrderStatus(request):
	userId = request.GET.get("userMessengerId")
	jsonData = {}
	data = {}
	queryOrder = Order.objects.filter(customer=userId, state="ONC")
	if queryOrder:
		currentOrder = queryOrder.first().pk
		currentState = "ONC"
	else:
		newOrder = Order(state="NEW",
				customer=userId,
				date=datetime.today(),
				payment_method = "CASH",
				delivery_address = "",
				subtotal = 0,
				shipping_cost = 3500,
				total_tax = 0,
				total_cost = 0)
		newOrder.save()
		currentOrder = newOrder.pk
		currentState = "NEW"
	data["currentOrder"] = currentOrder
	data["currentState"] = currentState
	jsonData["set_attributes"] = data
	return HttpResponse(json.dumps(jsonData, indent=4), content_type="application/json")

def getPreviousOrder(request):
	userId = request.GET.get("userMessengerId")
	orderId = Order.objects.filter(customer=userId, state="ONC").first().pk
	items = OrderItems.objects.filter(order__pk=orderId)
	json_data = {}
	messages = []
	attachment = {}
	payload = {}
	address = {}
	summary = {}
	elements = []
	payload["template_type"] = "receipt"
	payload["recipient_name"] = str(userId)
	payload["order_number"] = str(orderId)
	payload["currency"] = "COP"
	payload["payment_method"] = "Efectivo"
	payload["order_url"] = "www.instagram.com/wlwzrd"
	payload["timestamp"] = "1539655759"
	address["street_1"] = "AV 2HN No 54N-05, Apto 503C"
	address["street_2"] = ""
	address["city"] = "Cali"
	address["postal_code"] = "760001"
	address["state"] = "VA"
	address["country"] = "CO"
	payload["address"] =  address
	payload["adjustments"] = [{"name":"Descuento ", "amount":0}]
	subtotal = 0
	for i in items:
		subtotal += (i.quantity*i.product.price)
		elements.append({"title": i.product.name, 
				"subtitle":i.product.description,
				"quantity":i.quantity,
				"price":i.product.price,
				"currency":"COP",
				"image_url":i.product.image_url})
	payload["elements"] = elements
	summary["subtotal"] = subtotal
	summary["shipping_cost"] = 3500
	summary["total_tax"] = 0
	summary["total_cost"] = subtotal + 3500
	payload["summary"] = summary
	attachment["type"] = "template"
	attachment["payload"] = payload
	messages.append({"attachment":attachment})
	json_data["messages"] = messages
	return HttpResponse(json.dumps(json_data, indent=4),content_type="application/json")


	
