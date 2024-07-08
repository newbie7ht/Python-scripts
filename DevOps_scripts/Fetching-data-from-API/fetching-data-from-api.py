#Fetching Data from an API
#This script fetches and prints data from a REST API.
import requests

def fetch_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        print("API Data:", response.json())
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

api_url = "https://api.example.com/data"
fetch_api_data(api_url)


############################output################################
API Data: {'id': 1, 'name': 'Harsh Trivedi', 'email': 'harsh.trivedi4321@gmai.com'}
