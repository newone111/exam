#weather condition in TelAviv
from bs4 import BeautifulSoup
import requests

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
	"Accept-Language": "en-US,en;q=0.5"}
 
params = {
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en" }
 
def weather(city):
	city = city.replace(" ", "+")
	res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers, params=params)
	soup = BeautifulSoup(res.text, 'html.parser')
	location = soup.select('#wob_loc')[0].getText().strip()
	time = soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_ttm')[0].getText().strip()
	wind = soup.select('#wob_tws')[0].getText().strip()
	humidity = soup.select('#wob_hm')[0].getText().strip()
	print("Current weather for "+location)
	print("Latest update at "+time)
	print(info) 
	print("Wind "+wind)
	print("Humidity "+humidity)
	print(weather+"°C")
	#print (res.text)
 
city = "TelAviv"
city = city+" weather"
weather(city)

