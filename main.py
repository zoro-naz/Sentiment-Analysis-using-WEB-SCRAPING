import requests
from bs4 import BeautifulSoup

def get_product_reviews(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    reviews = []
    for review in soup.find_all('div', class_='review'):
        review_text = review.find('span', {'data-asin': 'B09'}).text.strip()  # Adjust the tag & class
        reviews.append(review_text)
    
    return reviews

url = 'https://www.example.com/product-reviews'  # Replace with the actual URL
reviews = get_product_reviews(url)
print(reviews)
