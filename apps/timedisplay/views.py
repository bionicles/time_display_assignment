from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now
    context = {
        "now": now
    }
    return render(request, 'timedisplay/index.html', context = context)
