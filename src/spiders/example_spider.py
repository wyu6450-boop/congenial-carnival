import requests
from bs4 import BeautifulSoup

def scrape_example():
    url = "https://example.com"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Page title:", soup.title.string)
    else:
        print("Failed to fetch the URL")

if __name__ == "__main__":
    scrape_example()