import urllib.request, json 
with urllib.request.urlopen("https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD") as url:
	data = json.loads(url.read().decode())
	print(data[5]['spreadProfilePrices'][1]['bid'])

# with urllib.request.urlopen("https://api.telegram.org/bot2041486796:AAHe5rC_HQ64jCjXw6TgYx__W3pdp8OI4GE/sendMessage?chat_id=-1001540152981&text=1967.999") as url:
# 	data = json.loads(url.read().decode())
	# print(data[5]['spreadProfilePrices'][1]['bid'])