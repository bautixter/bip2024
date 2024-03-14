import requests

DEFAULT_URL = 'http://192.168.0.113:80/data'

def sendRequest(url = DEFAULT_URL):

    # Sending GET request
    response = requests.get(url)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Printing the response content (optional)
        print(response.text)
    else:
        # If the request was not successful, print an error message
        print(f"Error: {response.status_code}")