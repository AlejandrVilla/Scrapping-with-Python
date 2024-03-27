import re
import requests
from bs4 import BeautifulSoup

url = "https://alejandrvilla.github.io/Frontend_Mentor/results-summary-component-main/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.text)

result = soup.find("div", class_="summary")
divs = result.find_all("div")
patron = r'class\s*=\s*["\']([^"\']+)["\']'
clases = re.findall(patron, str(divs))

patron2 = r'<p>(.*?)</p>'
valores = [result.find("div", class_=valor).find_all("p") for valor in clases]
print(clases)
print(valores)

res = [re.findall(patron2, str(valor)) for valor in valores]
print(res)
for i in res:
    print(i[0], i[1], i[2])