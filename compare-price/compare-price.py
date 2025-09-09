import requests
from bs4 import BeautifulSoup
import pandas as pd
from operator import itemgetter

# Function to scrape products from your website
def scrape_website(base_url, num_pages):
    products = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}/page/{page}"  # Update based on your site's pagination logic
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract product details (update selectors as per your site)
            for product in soup.select(".product-item"):
                name = product.select_one(".product-name").text.strip()
                # Assuming each product has a unique URL
                link = product.select_one("a")['href']
                products.append({"name": name, "link": link})
        else:
            print(f"Failed to fetch page {page}")
    return products

# Function to scrape price from Amazon (or use API)
def get_amazon_price(product_name):
    search_url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Update selector for price based on Amazon's structure
        price = soup.select_one(".a-price-whole")
        if price:
            return int(price.text.replace(',', ''))
    return None

# Main script
def main():
    base_url = "https://publicissapient.360reward.co/mall/facets/623/plateau/7246?fromSuggestions=false&page=1"  # Replace with your website
    num_pages = 113

    # Step 1: Scrape products from your website
    products = scrape_website(base_url, num_pages)

    # Step 2: Compare prices on Amazon
    for product in products:
        product['price'] = get_amazon_price(product['name'])

    # Step 3: Filter and sort by price
    products_with_prices = [p for p in products if p['price'] is not None]
    top_100 = sorted(products_with_prices, key=itemgetter('price'), reverse=True)[:100]

    # Step 4: Save or display the results
    df = pd.DataFrame(top_100)
    df.to_csv("top_100_products.csv", index=False)
    print("Top 100 products saved to top_100_products.csv")

if __name__ == "__main__":
    main()