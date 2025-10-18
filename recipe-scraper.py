import requests
from bs4 import BeautifulSoup

# URL of the recipe page
urls = ["https://www.wwf.org.uk/recipes/quinoa-power-pot", "https://www.wwf.org.uk/recipes/banana-spelt-loaf-cake", "https://www.wwf.org.uk/recipes/carrot-chickpea-burgers", "https://www.wwf.org.uk/recipes/spinach-chickpea-falafel-wrap"]

def scrape_recipe(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        if response.status_code != 200:
            return f"Failed to retrieve the page. Status code: {response.status_code}"
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract recipe title
        title_element = soup.find('h1')
        title = title_element.get_text(strip=True) if title_element else 'No title is found!'

        # Extract ingredients
        ingredients_list = soup.find('section', id='ingredients').find('ul')
        ingredients = [li.get_text(strip=True) for li in ingredients_list.find_all('li')] if ingredients_list else []

        # Extract times
        recipe_section = soup.find('section', id='recipe-info') or soup.find('section', id='recipe-data')
        if recipe_section:
            time_element = recipe_section.find('div', class_='time')
            time = time_element.get_text(strip=True) if time_element else 'Time not found'
        else:
            time = 'Time not found'
        
        # Dicitionary
        return {
            'title': title,
            'ingredients': ingredients,
            'time': time
        }
    except Exception as e:
        return f"An error occured: {e}"

# Scrape each recipe and print the results
for url in urls:
    print(f"Scraping recipe from: {url}")
    print(scrape_recipe(url))
