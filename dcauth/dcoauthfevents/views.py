from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
import requests
import os

req_url_dc= "https://discord.com/api/oauth2/authorize?client_id=854428679145127937&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fdcoauthfevents%2Flogin%2Freq&response_type=code&scope=guilds.join%20guilds%20identify%20email"

# Create your views here.
def home(req:HttpRequest)-> JsonResponse:
    return JsonResponse({"msg": "fuck you"})

def dclogin(req:HttpRequest):
    return redirect(req_url_dc)
def dclogin_req(req:HttpRequest):
    code= request.GET.get('code')
    print(code)
    exc_code(code)
    return JsonResponse({'msg': 'You are actually not meant to see this! Well Hi Random Stranger, you found a Easter-Egg. You will be shortly redirected!'})

def exc_code(code:str):
    data ={
        "client_id": os.environ.get('dcu2_clid'),
        "client_secret": os.environ.get('dcu2_clscrt'),
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/userauth/login/redirect",
        "scope": "identify email guilds guilds.join"
    }
    headers ={
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp =requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    print(resp)
    credents= resp.json()
    print(credents)