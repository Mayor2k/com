from django.shortcuts import render
from api.models import *

def dashboard(request):

    data = {
        "items" : Order.objects.all()
    }

    return render(request, "index.html", data)
