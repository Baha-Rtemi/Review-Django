import datetime

from django.shortcuts import render

# Create your views here.

now = datetime.datetime.now()
def index(request):
    return render(request, "newyear/index.html", {
        "newyear": now.day == 1 and now.month == 1
        # try it:
        # "newyear": True
    })