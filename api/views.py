from django.http import HttpRequest, JsonResponse
from tinydb import TinyDB,Query
from tinydb.database import Document
db = TinyDB('db.json')
db=db.table("grocery")
q = Query()
import json
data = {
    1: {
        'name': 'Milk',
        'price': 2.5,
        'quantity': 10
    },
    2: {
        'name': 'Bread',
        'price': 1.5,
        'quantity': 20
    },
}
# Grocery store API
# GET /grocery - this endpoint will display a list of fruits.
# POST /grocery/add - this endpoint will display a form that allows users to add new fruits to the list.
# GET /grocery/type/<type> - this endpoint will display a list of fruits by specifying the fruit type in the URL.
# GET /grocery/name/<name> - this endpoint will display a list of fruits by specifying the fruit name in the URL.
# GET /grocery/price/<price> - this endpoint will display a list of fruits by specifying the fruit price in the URL.

def get_all_items(request: HttpRequest):
    return JsonResponse({"result": db.all()})

def get_add_fruits(request: HttpRequest):
    if request.method=='POST':
        data=request.body
        data=json.loads(data)
        db.insert(data)
        return JsonResponse({"result": db.all()})
    else:
        return JsonResponse({"status":"method error"})
    
def get_fruits_type(request: HttpRequest,type):
    return JsonResponse({"result": db.search(q.type == type)})

def get_fruits_name(request: HttpRequest, name):
    return JsonResponse({"result":db.search(q.name == name)})

def get_fruits_price(request: HttpRequest, price):
    return JsonResponse({"result":db.search(q.price == price)})





