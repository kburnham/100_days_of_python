



import requests
from twilio.rest import Client


# response = requests.get(url = 'http://api.open-notify.org/iss-now.json')

# response.raise_for_status()

# print(response.json())

twilio_number = '+17752966524'
twilio_account_sid = 'AC482479ab09970b55194dcae99d6a5d5b'
twilio_auth_token = 'd336a743ad8740d54713550454e5ada1'



# Austin
MY_LAT = 30.267153
MY_LONG = -97.743057

# san fran
# MY_LAT = 37.46
# MY_LONG = -122.25

#london
# MY_LAT = 51.30
# MY_LONG = -0.7


API_KEY='4cf2c482013f7af9d7dd2d917f918e28'
EXCLUDE='current,minutely,daily'


parameters = {"lat": MY_LAT, "lon": MY_LONG, 'appid':API_KEY, 'exclude':EXCLUDE}
response = requests.get('https://api.openweathermap.org/data/3.0/onecall', params = parameters)

# response = requests.get('https://api.openweathermap.org/data/2.5/weather', params = parameters)
response.raise_for_status()
# print(response.json())

results = response.json()
# print(results)


# results['daily'][0]['weather'][0]['id'] < 700

next_12 = results['hourly'][0:12]



ids = [h['weather'][0]['id'] for h in next_12]

print(ids)

desc = [h['weather'][0]['main'] for h in next_12]
print(desc)

outcome = [id for id in ids if id < 800]

print(outcome)

if len(outcome) > 0:

    msg = 'bring an umbrella'
    
else:
    msg = 'all clear'
    

client = Client(twilio_account_sid, twilio_auth_token)

message = client.messages \
                .create(
                    body=msg,
                    from_=twilio_number,
                    to='+15125966958'
                )

print(message.sid)

