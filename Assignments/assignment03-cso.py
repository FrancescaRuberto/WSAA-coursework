import requests

# Define the API endpoint (URL) for the required dataset
url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en'

# Send request to get the data
response = requests.get(url)