import requests


APP_ID = '929d0e1c'
API_KEY = '38d4a2389bd9c7fb444fb17724af07cc'

nutri_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_config = {
 "query":"ran 3.1 miles",
 "gender":"male",
 "weight_kg":"97",
 "height_cm":187.96,
 "age":50
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}


response = requests.post(url=nutri_endpoint, json=exercise_config, headers=headers)
print(response.text)

