import urllib.request, urllib.parse, urllib.error
import json
import requests
import ssl


api_key = 42

serviceurl = "http://py4e-data.dr-chuck.net/json?"


while True:
    print()
    address = input("Enter Location: ")
    if address == "quit" or address == "q":
        break

    parms = dict()
    parms["address"] = address

    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print("***********************")
    print(url)
    
    data = requests.get(url).json()

    status = data["status"]
    print("API Status: " + status)
    print()
    
    if status == "OK":
        for each in data["results"][0]["address_components"]:
            print(each["long_name"])
            
        formatted_address = data["results"][0]["formatted_address"]
        print()
        print(formatted_address)
        print("********************")

