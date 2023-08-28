import requests

def perform_request(countryName):
    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"name":countryName}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "fe84e350aamsh54bfb10d766e2e1p1e50e5jsna8c82ecc0b6d"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()