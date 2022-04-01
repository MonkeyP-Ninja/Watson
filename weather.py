import json
import requests

apiKey= 'f4e28220a8a15d2ab9d55689a3de122d'



params = {
  'access_key': '03ad22a62fe86b318f9c17b2fc739c62',
  'query': 'Metz'
}

api_result = requests.get('api.openweathermap.org/data/2.5/forecast?lat=35&lon=139&appid={f4e28220a8a15d2ab9d55689a3de122d}')

list=api_result.json()



print(list)


