import requests
from bs4 import BeautifulSoup
import re
import json

# The final link does not play in VLC player at this time (July 12 2020)
# It works in Quicktime Player

# Grab JSON in page source
url = 'https://ch3plus.com/live'
request = requests.get(url)
html = request.text
soup = BeautifulSoup(html, 'html.parser')
ch3_script = str(soup.find(id='__NEXT_DATA__'))
ch3_json = re.findall('{.+}', ch3_script)
ch3_json = ch3_json[0]
ch3_json = json.loads(ch3_json)

# Get final URL
ch3thailand_m3u8 = ch3_json['props']['initialState']['liveReducer']['live']['streamUrl']