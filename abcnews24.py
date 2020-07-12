import requests
from bs4 import BeautifulSoup
import re
import json

# Grab all script elements on page as a string
url = 'https://www.abc.net.au/news/newschannel/'
request = requests.get(url)
html = request.text
soup = BeautifulSoup(html, 'html.parser')
abc_script = str(soup.body.script)

# Get JSON from inside the script elements and convert it into proper JSON format
abc_json = re.findall('{.+}', abc_script)
abc_json = abc_json[0]
abc_json = abc_json.replace('\'', '"')
abc_json = json.loads(abc_json)

# Get final URL
abc_m3u8 = abc_json.get('url')