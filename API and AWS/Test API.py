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

# Replace '[TOKEN]' with your actual token
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtpZEtleSJ9.eyJkYXRhIjp7Im5hbWUiOiJWZXNzZWxfdHJhY2tlciIsInVzZXJJZCI6MzQ4ODcsImFwcGxpY2F0aW9uTmFtZSI6IlZlc3NlbF90cmFja2VyIiwiaWQiOjE3NDUsInR5cGUiOiJ1c2VyLWFwcGxpY2F0aW9uIn0sImlhdCI6MTcyMzAzOTU2NywiZXhwIjoyMDM4Mzk5NTY3LCJhdWQiOiJnZnciLCJpc3MiOiJnZncifQ.WB7k3C3a3KHO_2ngKPwH2vMGlKHgLWZRZJ0KZJU3e0_zHcFYpcrRgBzXSSw0Df6UIu_t8RlEBG9sA2H80MTZf4RglMzHjzdr4QaGj1-O2PQV-12gj7YeP5bPuQVIm_ZPr48d5k4uXoL2TVorBxY3BpS8B3S7ZGYOcKRPYuSwA5T66d8E2XCUbIWk9PZ7hdaCgHaiZIatjV-RfWVZTagrTe01FfiBPLpMgrkfa25TNAJYcuHDB9XTUZnbdgcqe_M4FiD1W5LNNjrOSN4fa4FbF8HMEgk51pP6ocpgHMSU8zhOnhAetWwlWw_1qXPnsant0vG6kg4ZCJ6chNMLMB_A5gRwB2hww4R5RZ5BUsbCQp2mnXvo-j_G4RBC3ingg292G6Uir2JWst6hY6kMJVlTOxLnUziaSii8fisHK3BiBNh66AFxYk7qYBrrsa0HjXypdhW1JJt7ULfXMlq97Zh5fYlgR_XIsppLfaZ8qfoumgFkxCPzJDrA2wpdyX_J3x9z'

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
