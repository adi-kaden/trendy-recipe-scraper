import requests

from bs4 import BeautifulSoup
url = "https://www.wwf.org.uk/recipes/quinoa-power-pot"

response = requests.get(url)
print(f"Response status code: {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:200])

title_element = soup.find('h1')
title = title_element.get_text(strip=True) if title_element else 'No title is found!'
print(f"Recipe Title: {title}")

ingredients_list = soup.find('section', id='ingredients').find('ul')
ingredients = [li.get_text(strip=True) for li in ingredients_list.find_all('li')] if ingredients_list else []
print("Ingredients:")
for ingredient in ingredients:
    print(f"- {ingredient}")
    
