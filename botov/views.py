from django.shortcuts import render
from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from math import pow
from datetime import datetime
import pytz
import json
import requests
import wget

# Create your views here.

def index(request):
	return HttpResponse("JulietaLabs's API services for BOT")

def download_image(url):
        IMAGE_FOLDER = "media/images"
        image_path = wget.download(url, out=IMAGE_FOLDER)
        return image_path

def call_service_post(image_path):
        api_key = "acc_84d9408967d5379"
        api_secret = "706560073a04cc1a3e2ec3cf7aad5d77"
        response = requests.post(
    'https://api.imagga.com/v2/tags',
    auth=(api_key, api_secret),
    files={'image': open(image_path, 'rb')})
        return response

def call_service_get(image_url):
        api_key = "acc_84d9408967d5379"
        api_secret = "706560073a04cc1a3e2ec3cf7aad5d77"
        response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))
        return response

def callService(img_url):
        url = "https://api.imagga.com/v2/tags"
        querystring = {"image_url":img_url, "version":"2"}
        headers = {
        'accept': "application/json",
        'authorization': "Basic YWNjXzg0ZDk0MDg5NjdkNTM3OTo3MDY1NjAwNzNhMDRjYzFhM2UyZWMzY2Y3YWFkNWQ3Nw=="
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response


def getTags(recognition):
        words = ""
        for i in [0,1,2,3]:
                words = words + recognition.json()["result"]["tags"][i]["tag"]["en"] + ", "
        return words

#@csrf_exempt
def getImageRecognition(request):
        #image =  request.body
        #image_url = json.loads(image)["image_url"]
        #image_path = download_image(img_url)
        image_url = request.GET.get("image_url")
        recognition = callService(image_url)
        status = recognition.json()["status"]["type"]
        json_data = {}
        text = {}
        data = []
        if status == "success":
                words = getTags(recognition)
        else:
                words = "Recognition  failed due to an error. The server does not support the URL: " + image_url
        text["text"] = "Your photo is: " + words 
        data.append(text) 
        json_data["messages"] =  data
        return HttpResponse(json.dumps(json_data, indent=4), content_type="application/json")



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


