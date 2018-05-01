import requests
import datetime
import json
import csv
import re
from os import environ

POST_URL = 'https://api.groupme.com/v3/bots/post'

MESSAGE_URL = 'https://api.groupme.com/v3/groups/33175999/messages' # Real
# MESSAGE_URL = 'https://api.groupme.com/v3/groups/40429304/messages' # Test

PARAMS = {'token': 'RQmeVuHtocjtAcGmgTHYR1BL3g1lBCiGJgz55Act'}
HEADERS = {'content-type': 'application/json'}

BOT_ID = '0aafafce1aef34384b7bb45233' # real
# BOT_ID = '55d836eb2b95f01b990614ad1c' # test

DATA = {
    'text': 'Proper',
    'bot_id': BOT_ID
}


def main():

    flag = 0
    response = requests.get(MESSAGE_URL, params=PARAMS, headers=HEADERS).json()
    for message in response['response']['messages']:
        if re.search('@dinobot', message['text'], re.IGNORECASE) and message['name'] == 'Jamsheer Anklesaria':
            requests.post(POST_URL, data=json.dumps(DATA), headers=HEADERS)
        elif message['sender_type'] == 'bot':
            return


if __name__ == '__main__':
    main()
