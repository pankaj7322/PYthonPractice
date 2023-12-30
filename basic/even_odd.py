import requests

# Replace 'YOUR_API_KEY' and 'YOUR_ENDPOINT' with the actual API key and endpoint
api_key = '545f672b6fd947598f35250c9e64fc07'                   
endpoint = 'https://newsapi.org/v2/top-headlines'

# Example API request using the requests library
def fetch_data_from_api():
    try:
        # Construct the API URL
        url = f'{endpoint}?apiKey={api_key}&country=us'

        # Make a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the response
            data = response.json()

            # Process the data as needed
            print(data)

        else:
            # Print an error message if the request was not successful
            print(f'Error: {response.status_code}')
            print(response.text)

    except Exception as e:
        print(f'An error occurred: {e}')

# Call the function to fetch data from the API
fetch_data_from_api()
