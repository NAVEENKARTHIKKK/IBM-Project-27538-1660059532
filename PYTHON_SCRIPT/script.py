import requests
a="https://api.openweathermap.org/data/2.5/weather?lat=9.939093&lon=78.121719&appid=774e289f963ae64e2b43500df7bd1053"
r = requests.get(url=a)
data = r.json()
print(r)
print(data)
temp = data["main"]["temp"]
hum = data["main"]["humidity"]
print("Temperature is :",temp)
print("Humidity is :",hum)
