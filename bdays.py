import requests
import datetime
import json
import csv
from os import environ

# app = Flask(__name__)
# app.run(environ.get('PORT'))

birthday_data = (
    ['Erica', 'Abramson', '6/21/17'],
    ['Bolu', 'Adeyeye', '12/22/17'],
    ['Matt', 'Ale', '6/26/17'],
    ['Khalid', 'Almoammar', '2/10/17'],
    ['Josh', 'Andermarch', '12/12/17'],
    ['Jamsheer', 'Anklesaria', '6/7/17'],
    ['Mio', 'Asatani', '6/27/17'],
    ['Dara', 'Blume', '8/13/17'],
    ['Benny', 'Bursztyn', '10/20/17'],
    ['Pranav', 'Chachra', '11/3/17'],
    ['Justin', 'Charles', '12/5/17'],
    ['Lisa', 'Chen', '12/21/17'],
    ['April', 'Chye', '4/16/17'],
    ['Jose', 'Clautier', '3/17/17'],
    ['Anya', 'Clifford', '5/24/17'],
    ['Maor', 'Cohen', '7/22/17'],
    ['Daniel', 'Dall Acqua', '7/12/17'],
    ['Greg', 'Doger de Speville', '1/15/17'],
    ['Hannah', 'Dolgin', '11/28/17'],
    ['Gillian', 'Dudeck', '7/15/17'],
    ['Evan', 'Einstein', '4/10/17'],
    ['Matt', 'Ellis', '12/11/17'],
    ['Mike', 'Flum', '3/9/17'],
    ['Kevin', 'Gallagher', '10/18/17'],
    ['Mitch', 'Gorodokin', '5/10/17'],
    ['Lindley', 'Gray', '8/25/17'],
    ['Anchal', 'Gulati', '2/22/17'],
    ['Oscar', 'Hentschel', '11/4/17'],
    ['Morgan', 'Holmes', '7/13/17'],
    ['Keita', 'Ito', '4/4/17'],
    ['Nick', 'Karr', '11/23/17'],
    ['Liz', 'Kelley', '9/23/17'],
    ['Erik', 'Kogut', '12/18/17'],
    ['Minsu (Brandon)', 'Kong', '1/3/17'],
    ['Joon', 'Lee', '6/4/17'],
    ['Joe', 'Lin', '8/20/17'],
    ['Jeffrey', 'Lothian', '2/26/17'],
    ['Sandra', 'Lucia', '2/13/17'],
    ['Joe', 'Lynch', '11/12/17'],
    ['Liz', 'McCue', '3/29/17'],
    ['Gabriel', 'Metzger', '6/24/17'],
    ['Will', 'Miller', '12/15/17'],
    ['Cyrus', 'Mojdehi', '2/8/17'],
    ['Mark', 'Mosby', '2/1/17'],
    ['Amelia', 'Munson', '12/22/17'],
    ['Gladys', 'Ndagire', '10/2/17'],
    ['Kelly', "O'Brien", '12/24/17'],
    ['Andrea', 'Oran', '9/18/17'],
    ['Valentina', 'Pardo', '11/12/17'],
    ['Alexa', 'Picciotto', '1/31/17'],
    ['Adi', 'Prasad', '9/3/17'],
    ['Justin', 'Reggi', '5/12/17,'],
    ['Laura', 'Rodgers', '4/2/17'],
    ['Eytan', 'Schindelhaim', '10/22/17'],
    ['Janaki', 'Sekaran', '1/2/17'],
    ['Sid', 'Shanbhag', '7/9/17'],
    ['Sarah', 'Shenker', '1/16/17'],
    ['David', 'Streger', '4/25/17'],
    ['Vincent', 'Su', '10/4/17'],
    ['Maeve', 'Tsivanidis', '8/8/17'],
    ['Naomi', 'Tudhope', '8/24/17'],
    ['Nivedita', 'Venkateish', '7/24/17'],
    ['Rachel', 'Wasser', '4/26/17'],
    ['Jasper', 'Wu', '12/25/17'],
    ['Frank', 'Yodice', '6/6/17'],
    ['Zenah', 'Hasan', '2/1/17'],
    ['Vicci', 'Zhong', '8/19/17'],
    ['Sherie', 'Zhou', '8/17/17'],
)

URL = 'https://api.groupme.com/v3/bots/post'

# Cluster D group Bot
BOT_ID = '0aafafce1aef34384b7bb45233'

# Test Bot
# BOT_ID = '9ed43f52fe4c724c362063c5de'

HEADERS = {'content-type': 'application/json'}

BDAYS_INPUT = 'bdays.csv'


def bdays(birthday_data, today):
    todays_bdays = []
    for row in birthday_data:
        bday = row[2]
        bday = bday.split('/')
        month = bday[0]
        day = bday[1]
        if int(month) == today.month and int(day) == today.day:
            todays_bdays.append(row)

    for todays_bday in todays_bdays:
        first_name, last_name = todays_bday[0], todays_bday[1]
        data = {
            'bot_id': BOT_ID,
            'text': 'Happy birthday @{} {}!!!'.format(first_name, last_name)
        }
        print(data)
        response = requests.post(URL, data=json.dumps(data), headers=HEADERS)
        print(response.content)


def main():
    today = datetime.datetime.now()
    bdays(birthday_data, today)


if __name__ == '__main__':
    main()
