import requests
import json

response = requests.get("http://localhost:8000/apioverview/monthly-package/")
print(response)
json_data = response.json()['results']['package_name']
print(json_data)