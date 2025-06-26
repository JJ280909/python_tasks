import requests 


response = requests.get('http://open-notify.org/Open-Notify-API/')
print(response)
json = response.json()

print(json)