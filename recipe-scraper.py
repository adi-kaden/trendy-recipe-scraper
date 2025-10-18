import requests
from bs4 import BeautifulSoup

# URL of the recipe page
url = "https://www.wwf.org.uk/recipes/quinoa-power-pot"

# Send a GET request to the URL
response = requests.get(url)
print(f"Response status code: {response.status_code}")

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract recipe title
title_element = soup.find('h1')
title = title_element.get_text(strip=True) if title_element else 'No title is found!'

# Extract ingredients
ingredients_list = soup.find('section', id='ingredients').find('ul')
ingredients = [li.get_text(strip=True) for li in ingredients_list.find_all('li')] if ingredients_list else []
print("Ingredients:")
for ingredient in ingredients:
    print(f"- {ingredient}")

# Extract times
time_element = soup.find('section', id='recipe-info').find('div', class_='time').text
