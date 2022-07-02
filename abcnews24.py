import requests
from bs4 import BeautifulSoup
import re
import json

# Grab all script elements on page as a string
url = 'https://www.abc.net.au/news/newschannel/'
request = requests.get(url)
html = request.text
soup = BeautifulSoup(html, 'html.parser')
abc_script = str(soup.find_all('script'))

# Get JSON from inside the script elements and convert it into proper JSON format
abc_json = re.findall('window.__API__ = {.+}', abc_script)
abc_json = re.findall('{.+}', abc_json[0])
abc_json = json.loads(abc_json[0])

# Grab m3u8 link 
abc_m3u8 = abc_json['channelpage']['components'][0]['component']['props']['video']['config']['sources'][0]['file']