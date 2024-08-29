import requests
import json

# Define the API endpoint
url = 'https://gateway.api.globalfishingwatch.org/v3/events'

# Define the parameters for the GET request
params = {
   # 'vessels[0]': '9b3e9019d-d67f-005a-9593-b66b997559e5',
    'datasets[0]': 'public-global-fishing-events:latest',
    'start-date': '2017-01-01',
    'end-date': '2017-01-31',
    'limit': 100,
    'offset': 0
}


token = ''
# Define the headers, including the authorization token
headers = {
    'Authorization': f'Bearer {token}'
}

# Make the GET request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Define the path to save the JSON file
    file_path = 'ship_data.json'
    
    # Write the JSON data to a file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Data successfully saved to {file_path}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print(response.text)
