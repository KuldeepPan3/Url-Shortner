from django.shortcuts import render, HttpResponse, redirect
from .models import  UrlModel
import string
import random
# Create your views here.
def home(request):
    return render(request, 'home.html')
def shorturls(request):
    if request.method == 'POST':
        longurl = request.POST['longurl']
        stringurl = string.ascii_letters + string.digits
        shorturl = ''.join(random.choice(stringurl) for i in range(7))
        obj = UrlModel.objects.create(longurl= longurl, shorturl=shorturl)
        print("Long url is created", obj)
        shorturl = "http://127.0.0.1:8000/"+shorturl

    #return HttpResponse(f'Your shorturl for {longurl} is {shorturl}')
    return render(
        request, "home.html", {"shorturl": shorturl, "longurl": longurl}
    )

def redirecturl(request, shorturl):
    try:
        obj = UrlModel.objects.get(shorturl=shorturl)
    except UrlModel.DoesNotExist:
        obj = None
    if obj is not None:
        obj.count+=1
        obj.save()
        print(obj)
        longurl = obj.longurl
        return redirect(longurl)
    else:
        return HttpResponse("Invalid Url")
