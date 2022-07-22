from django.shortcuts import render
import requests

def home(request):
    context={}
    if request.method == 'GET':
        context['button_text'] = 'Quiero mi regalo!'
    elif request.method == 'POST':
        r=requests.get('https://randomfox.ca/floof/')
        data=r.json()
        context['button_text'] = 'Quiero más!'
        context['url']= data["image"]  
    return render(request, 'foxes/index.html',context)