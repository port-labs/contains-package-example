## Import the needed libraries
import requests
import os

# Get environment variables using os.environ["KEY"]
PORT_CLIENT_ID = os.environ["PORT_CLIENT_ID"]
PORT_CLIENT_SECRET = os.environ["PORT_CLIENT_SECRET"]
PATH_TO_REQUIREMENTS_TXT_FILE = os.environ["PATH_TO_REQUIREMENTS_TXT_FILE"]
PORT_API_URL = "https://api.getport.io/v1"
blueprint_id = 'package'


## Get Port Access Token
credentials = {'clientId': PORT_CLIENT_ID, 'clientSecret': PORT_CLIENT_SECRET}
token_response = requests.post(f'{PORT_API_URL}/auth/access_token', json=credentials)
access_token = token_response.json()['accessToken']

# You can now use the value in access_token when making further requests
headers = {
	'Authorization': f'Bearer {access_token}'
}

def add_entity_to_port(entity_object):
    """A function to create the passed entity in Port

    Params
    --------------
    entity_object: dict
        The entity to add in your Port catalog
    
    Returns
    --------------
    response: dict
        The response object after calling the webhook
    """
    response = requests.post(f'{PORT_API_URL}/blueprints/{blueprint_id}/entities?upsert=true&merge=true', json=entity_object, headers=headers)
    print(response.json())

def read_and_parse_requirements_file():
    """This function reads the content of the requirements.txt file and sends the resulting entity to Port"""

    with open(PATH_TO_REQUIREMENTS_TXT_FILE, 'r') as file:
        package_list = file.readlines()

    package_string = ' '.join(package_list).replace('\n', '')

    entity = {
    "identifier": "my_requirement_file",
    "title": "Python Requirements File",
    "properties": {
        "content": package_string
    },
    "relations": {}
    }

    add_entity_to_port(entity_object=entity) ## send the data to Port

read_and_parse_requirements_file()