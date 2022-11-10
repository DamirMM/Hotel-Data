import requests

url = "https://hotels4.p.rapidapi.com/locations/v3/search"

querystring = {"q":"ljubljana","locale":"en_US","langid":"1033","siteid":"300000001"}

headers = {
	"X-RapidAPI-Key": "a71fb91a78msh2b907940678c168p1c4174jsn9d851e261b05",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)