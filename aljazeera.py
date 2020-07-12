import requests
import json

# URL and headers for request
url = "https://edge.api.brightcove.com/playback/v1/accounts/665003303001/videos/5467349513001"
headers = {
	"Accept" : "application/json;pk=BCpkADawqM39agLpp-TuKJ3fi2ac40ghRBmnV3-bKKuO6oZSDAbOgt4HRS5TzFxLH2NA0XQdsoWQjrOYvmD2bVLQSYjxRgHufXokniy4kOamHBQs6UIbDSYvj2M",
}

# Make request. The returned content is already in JSON format containing the m3u8 link
request = requests.get(url, headers=headers).json()

# Get final URL
aljazeera_m3u8 = request['sources'][0]['src']