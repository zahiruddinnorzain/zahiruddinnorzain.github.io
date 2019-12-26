import urllib.request, json

num = input("number = ")
#int(num)
#print(type(num))

with urllib.request.urlopen("https://samples.openweathermap.org/data/2.5/forecast/hourly?zip=48000&appid=31ba122c59712c211cc6dcad08b29c51") as url:
	data = json.loads(url.read().decode())
	print(data["list"][int(num)]["weather"][0]["main"])
	print(data["city"]["name"])
	print(data["list"][1]["dt_txt"])


#https://openweathermap.org/api/hourly-forecast
