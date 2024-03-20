import requests
from pprint import pprint
space = '6wt3eguomfd7'
access_token = 'TLrijUQGJDq5lUu0NTHZSSLzC9F5yOnxlKDB0CDYbq0e'

# Define the Contentful API endpoint
api_url = f'https://cdn.contentful.com/spaces/{space}/entries'

# Define headers including access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Send GET request to Contentful API
response = requests.get(api_url, headers=headers)

# Check if the request was successful
if response.ok:
    # Extract JSON data from the response
    data = response.json()
    # Process the retrieved data as needed
    pprint(data)
else:
    # Print error message if request was not successful
    print(f"Error: {response.status_code} - {response.text}")
