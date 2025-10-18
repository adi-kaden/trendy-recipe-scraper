import requests

from bs4 import BeautifulSoup
url = "https://www.wwf.org.uk/recipes/quinoa-power-pot"

response = requests.get(url)
print(f"Response status code: {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:200])
