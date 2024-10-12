from selenium import webdriver
from bs4 import BeautifulSoup
import json

# Initialize the Selenium WebDriver (make sure the correct path to the WebDriver is provided)
driver = webdriver.Chrome()

# Open the product listing page
driver.get('https://www.microfocus.com/en-us/products?trial=true')

# Parse the page content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Initialize the product list
products = []

# Find all product cards (modify the selector as necessary)
product_cards = soup.find_all('div', class_='uk-card')
for card in product_cards:
    #print(card.prettify())
    product_name = card.find('h3', class_='uk-card-title').text.strip()
    description = card.find('div', class_='description').find('p').text.strip()
    trial_link = card.find('a', class_='uk-button-primary')['href']

    community_link="N/A"
    support_link = "N/A"
    temp = card.find('a', string='Support',target='_blank')
    if temp:
        print(temp)
        support_link = temp['href']
    temp2 = card.find('a', string='Community',target='_blank')
    if temp2 and temp2.has_attr('href'):
        print(temp2.text.strip())
        community_link = temp2['href']
    product = {
        "Product Name": product_name,
        "Starting Letter": product_name[0].upper(),
        "Description": description,
        "Free Trial / Demo Request URL": trial_link,
        "Support Link URL": support_link,
        "Community Link URL": community_link
    }
    products.append(product)

# Save to JSON file
with open('products.json', 'w') as f:
    json.dump(products, f, indent=4)

print("Product data saved to products.json")

# Close the driver
driver.quit()
