import requests
import urllib3
import json
#import utils

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

from config import WEBEX_TEAMS_URL, WEBEX_TEAMS_AUTH, WEBEX_TEAMS_ROOM, WEBEX_BOT_ID

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


def get_room_id(room_name):
    """
    This function will find the Webex Teams space id based on the {space_name}
    Call to Webex Teams - /rooms
    :param room_name: The Webex Teams room name
    :return: the Webex Teams room Id
    """
    room_id = None
    url = WEBEX_TEAMS_URL + '/rooms' + '?max=1000'
    header = {'content-type': 'application/json', 'authorization': WEBEX_TEAMS_AUTH}
    space_response = requests.get(url, headers=header, verify=False)
    space_list_json = space_response.json()

    space_list = space_list_json['items']
    for spaces in space_list:
        if spaces['title'] == room_name:
            room_id = spaces['id']
    return room_id


def post_room_message(space_name, message):
    """
    This function will post the {message} to the Webex Teams space with the {space_name}
    Call to function get_space_id(space_name) to find the space_id
    Followed by API call /messages
    :param space_name: the Webex Teams space name
    :param message: the text of the message to be posted in the space
    :return: none
    """
    space_id = get_room_id(space_name)
    payload = {'roomId': space_id, 'text': message}
    url = WEBEX_TEAMS_URL + '/messages'
    header = {'content-type': 'application/json', 'authorization': WEBEX_TEAMS_AUTH}
    requests.post(url, data=json.dumps(payload), headers=header, verify=False)


