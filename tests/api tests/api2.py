import requests

url = "https://transfermarket.p.rapidapi.com/clubs/get-squad"

querystring = {"id":"9636"}

headers = {
	"X-RapidAPI-Key": "24681b8eefmsh1701319ef803d55p15589ajsnbdf4e27530da",
	"X-RapidAPI-Host": "transfermarket.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)