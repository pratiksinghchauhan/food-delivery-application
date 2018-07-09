from django.shortcuts import render
import requests
import datetime
from .models import order_model
# Create your views here.
def renderIndex(request):
    if request.method=="POST":
        pnr = request.POST.get("pnr")
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        stationCode = request.POST.get("stationCode")

        #pnrStatus = requests.get("https://api.railwayapi.com/v2/pnr-status/pnr/"+ pnr +"/apikey/"+ apiKey )

        pnrStatus ={ 
                "response_code": 200,
                "debit": 3,
                "pnr": "1234567890",
                "doj": "25-6-2017",
                "total_passengers": 3,
                "chart_prepared": True,
                "from_station": {
                    "name": "Kopargaon",
                    "code": "KPG"
                },
                "to_station": {
                    "name": "Hazrat Nizamuddin",
                    "code": "NZM"
                },
                "boarding_point": {
                    "name": "Kopargaon",
                    "code": "KPG"
                },
                "reservation_upto": {
                    "name": "Hazrat Nizamuddin",
                    "code": "NZM"
                },
                "train": {
                    "name": "GOA EXPRESS",
                    "number": "12779"
                },
                "journey_class": {
                    "name": "SLEEPER CLASS",
                    "code": "SL"
                },
                "passengers": [
                    {
                    "no": 1,
                    "current_status": "RLWL/11",
                    "booking_status": "RLWL/39/GN"
                    },
                    {
                    "no": 2,
                    "current_status": "RLWL/12",
                    "booking_status": "RLWL/40/GN"
                    },
                    {
                    "no": 3,
                    "current_status": "RLWL/13",
                    "booking_status": "RLWL/41/GN"
                    }
                ]
                }

        trainNumber = pnrStatus["train"]["number"]
        print trainNumber

        #trainRoute = requests.get("https://api.railwayapi.com/v2/route/train/"+ train+ "/apikey/"+ apiKey)

        trainRoute = {
            "response_code": 200,
            "debit": 1,
            "train": {
                "name": "KLK-NDLS SHATABDI EXP",
                "number": "12006",
                "days": [
                {
                    "code": "MON",
                    "runs": "Y"
                },
                {
                    "code": "TUE",
                    "runs": "Y"
                },
                {
                    "code": "WED",
                    "runs": "Y"
                },
                {
                    "code": "THU",
                    "runs": "Y"
                },
                {
                    "code": "FRI",
                    "runs": "Y"
                },
                {
                    "code": "SAT",
                    "runs": "Y"
                },
                {
                    "code": "SUN",
                    "runs": "Y"
                }
                ],
                "classes": [
                {
                    "code": "3A",
                    "available": "N"
                },
                {
                    "code": "SL",
                    "available": "N"
                },
                {
                    "code": "1A",
                    "available": "N"
                },
                {
                    "code": "2S",
                    "available": "N"
                },
                {
                    "code": "FC",
                    "available": "N"
                },
                {
                    "code": "2A",
                    "available": "N"
                },
                {
                    "code": "CC",
                    "available": "N"
                },
                {
                    "code": "3E",
                    "available": "N"
                }
                ]
            },

            "route": [
                {
                "no": 1,
                "scharr": "SOURCE",
                "schdep": "06:15",
                "distance": 0,
                "halt": -1,
                "day": 1,
                "station": {
                    "name": "KALKA",
                    "code": "KLK",
                    "lng": "null",
                    "lat": "null"
                }
                },
                {
                "no": 2,
                "scharr": "06:45",
                "schdep": "06:53",
                "distance": 37,
                "halt": 8,
                "day": 1,
                "station": {
                    "name": "CHANDIGARH",
                    "code": "CDG",
                    "lng": "null",
                    "lat": "null"
                }
                },
                {
                "no": 3,
                "scharr": "07:33",
                "schdep": "07:38",
                "distance": 104,
                "halt": 5,
                "day": 1,
                "station": {
                    "name": "AMBALA CANT JN",
                    "code": "UMB",
                    "lng": "null",
                    "lat": "null"
                }
                },
                {
                "no": 4,
                "scharr": "08:10",
                "schdep": "08:12",
                "distance": 146,
                "halt": 2,
                "day": 1,
                "station": {
                    "name": "KURUKSHETRA JN",
                    "code": "KKDE",
                    "lng": "null",
                    "lat": "null"
                }
                },
                {
                "no": 5,
                "scharr": "10:20",
                "schdep": "DEST",
                "distance": 302,
                "halt": -1,
                "day": 1,
                "station": {
                    "name": "NEW DELHI",
                    "code": "NDLS",
                    "lng": "null",
                    "lat": "null"
                }
                }
            ]
            }


        for values in trainRoute["route"]:
            if(values["station"]["code"] == stationCode):
                break
        print values

        doj =   pnrStatus["doj"]
        trainTouchesStation = values["day"]
        deliveryDay = datetime.datetime.strptime(doj, "%d-%m-%Y") + datetime.timedelta(days=trainTouchesStation)
        deliveryDay = deliveryDay.strftime("%d-%m-%Y")
        expectedDeliveryTime = values["scharr"]
        expectedDeliveryTime =  datetime.datetime.strptime(expectedDeliveryTime, '%H:%M').time()

        instance = order_model(name=name,mobile_number=contact,pnr=pnr,delivery_station_code=stationCode,train_number=trainNumber,status="UNDELIVERED",exprected_delivery_time=exprectedDeliveryTime)
        instance.save()
        responseText = "Alright We got your order, "+ "if the train reaches on time you will get order on "+ deliveryDay + " between "+ values["scharr"] + " and " + values["schdep"] + " ,dont worry we will keep tracking the status and deliver hot food"
        print responseText
        return render(request,"index.html",{"responseText":responseText})


    return render(request,"index.html")

def checkDatabaseAndSendConfirmation(request):
    time_threshold = datetime.now() + timedelta(hours=3)
    orders = order_model.objects.fiter(status="UNDELIVERED",exprected_delivery_time__lt=time_threshold,isRestaurantNotified=False)
    for data in orders:
            #check live status and see if train is comming in next 2.5 hours or not and update db 
    return True

