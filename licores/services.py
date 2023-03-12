import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_licor(data):
    params ={'s': data}
    response = generate_request('https://www.thecocktaildb.com/api/json/v1/1/search.php?', params)
    if response:
       licor = response.get('drinks')[0]
       return licor

    return ""