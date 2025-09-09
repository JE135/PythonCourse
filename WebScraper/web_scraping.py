from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-gv-n308tgaming-oc-12gd-geforce-rtx-3080-ti-12gb-graphics-card-windforce-3x/p/N82E16814932436?cm_re=3080-_-14-932-436-_-Product&Description=3080"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)