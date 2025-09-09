from bs4 import BeautifulSoup
import requests

search_term = input("What product do you want to search for? ")

url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

results = []

for page_num in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page_num}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    divs = doc.find_all("div", class_="item-cell")
    
    for div in divs:
        title_tag = div.find("a", class_="item-title")
        if title_tag and search_term.lower() in title_tag.text.lower():
            link = title_tag['href']
            price_tag = div.find("li", class_="price-current")
            try:
                price = int(price_tag.strong.text.replace(",", ""))
            except:
                price = "Price not listed"
            
            results.append(f"{title_tag.text}\nPrice: {price}\nLink: {link}\n-------------------------------\n")

# Save results to a text file
with open(f"{search_term}_newegg.txt", "w", encoding="utf-8") as file:
    file.writelines(results)

print(f"Results saved to {search_term}_newegg.txt")
