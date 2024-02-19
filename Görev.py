import requests
from bs4 import BeautifulSoup
import json

def scrape_glassdollar():
    url = 'https://ranking.glassdollar.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        enterprises = []

        for enterprise in soup.find_all('div', class_='enterprise'):
            enterprise_data = {}
            enterprise_data['name'] = enterprise.find('h3').text.strip()
            enterprises.append(enterprise_data)

        return enterprises
    else:
        print("Failed to retrieve data from Glassdollar.")
        return []

if __name__ == "__main__":
    data = scrape_glassdollar()
    with open('glassdollar_data.json', 'w') as f:
        json.dump(data, f, indent=4)
