from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world!")


@csrf_exempt
def api(request):
    # if requested by get
    if request.method == 'GET':
        return HttpResponse("Error, use POST in stead of GET.")

    # get data from request
    data_get = json.loads(request.body)
    value1 = data_get["value1"]
    value2 = data_get["value2"]

    # return result as json
    data_send = {
        "value1": value1,
        "value2": value2
    }
    return JsonResponse(data_send)
