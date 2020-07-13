import requests
import json

# URL and headers for request
url = 'https://edge.api.brightcove.com/playback/v1/accounts/5282994675001/videos/6016428620001'
headers = {
    'Accept' : 'application/json;pk=BCpkADawqM3CPVbEhO4GPYxoVow9nFpCowmUGNmjtiejFS3u_zTIWInz4yWFqCeA876BkXmbu4p_raekK9zHb2uKOfFPBpp9KEkQ0ENMdoeQdKGI_qnnLjl4XcOmx3Iz7yAFaj2KkJnk43zF',
}

# Make request. The returned content is already in JSON format containing the m3u8 link
request = requests.get(url, headers=headers).json()

# Get final URL
ch7thailand_m3u8 = request['sources'][0]['src']