import requests
import json
import boto3

# Initialize the S3 client
s3_client = boto3.client('s3')

# Define the S3 bucket name
bucket_name = 'illegalfishing'
token = ''

# Define the API endpoint
url = 'https://gateway.api.globalfishingwatch.org/v3/events'

# Define the headers, including the authorization token
headers = {
    'Authorization': f'Bearer {token}'
}

def lambda_handler(event, context):
    for month in range(1, 13):  # Loop through each month in 2021
        start_date = f'2021-{month:02d}-01'
        end_date = f'2021-{month:02d}-{days_in_month(month)}'  # Get the correct last day of the month

        # Define the parameters for the GET request
        params = {
            'datasets[0]': 'public-global-fishing-events:latest',
            'start-date': start_date,
            'end-date': end_date,
            'limit': 1000,  # Adjust limit as necessary
            'offset': 0
        }

        # Make the GET request
        response = requests.get(url, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Define the S3 object key (file name)
            file_name = f'ship_data_{start_date}.json'

            # Convert data to JSON string
            json_data = json.dumps(data, indent=4)

            # Upload the JSON data to S3
            s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=json_data)

            print(f"Data for {start_date} successfully saved to S3 as {file_name}")
        else:
            print(f"Failed to retrieve data for {start_date}: {response.status_code}")
            print(response.text)

def days_in_month(month):
    # Determine the number of days in the given month for 2021
    if month == 2:  # February
        return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:  # All other months
        return 31
