

import requests
from datetime import datetime


pixela_endpoint = 'https://pixe.la/v1/users'

USERNAME = 'kburnham'
TOKEN = 'kjshdakgh9237590'

user_params = {

    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url = pixela_endpoint, json = user_params)

# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'


graph_config = {
    'id': 'graph1',
    'name': 'running',
    'unit': 'Km',
    'type': 'float',
    'color': 'sora'

}

headers = {
    'X-USER-TOKEN': TOKEN
}


response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
print(response.text)


pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'

DATE = datetime.strftime(datetime.today(), format = '%Y%m%d')


pixel_config = {
    'date': '20230128',
    'quantity': '5',
    
}


response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


edit_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1/20230128'


edit_config = {
    'quantity': '5'
}


response = requests.put(url=edit_endpoint, json=edit_config, headers=headers)
print(response.text)



response = requests.delete(url=edit_endpoint, headers=headers)
print(response.text)