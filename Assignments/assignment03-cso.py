# This program retrieves the dataset for the "exchequer account (historical series)" from the CSO 
# And stores it into a file called "cso.json"

import requests

# Define the API endpoint (URL) for the required dataset
url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en'

# Send request to get the data
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    with open('cso.json', 'w') as file:
        file.write(response.text)
else:
    print('Could not retrieve data:', response.status_code)
