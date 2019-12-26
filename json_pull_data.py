import urllib.request, json 
with urllib.request.urlopen("https://raw.githubusercontent.com/zahiruddinnorzain/zahiruddinnorzain.github.io/master/file.json") as url:
	data = json.loads(url.read().decode())
	print(data["city"])