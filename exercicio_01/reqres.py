import requests, json

response = requests.get("https://reqres.in/api/users/2")
json = response.json()

for key in json:
	print ("{}: {}".format(key, json[key]))

data = {
    "email": "sydney@fife",
    "password": "pistol"
}
response_p = requests.post("https://reqres.in/api/register", data=data)
print(response_p.json())


response_d = requests.delete("https://reqres.in/api/users/2")
print(response_d)