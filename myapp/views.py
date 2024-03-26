from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def my_static_array(request):
    data = {
        "array": [1, 2, 3, 4, 5]
    }
    return JsonResponse(data)
