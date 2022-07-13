from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try: 
	html = urlopen("https://www.github.com/abdelrhmanshokr")
except HTTPError as e:
	print(f"HTTP error: {e}")
except URLError as e:
	print(f"URL error: {e}")
else: 
	print(f"here is your result code {html.code}")