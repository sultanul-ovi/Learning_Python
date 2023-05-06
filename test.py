import requests
from bs4 import BeautifulSoup

username = "your_username_here"
url = "https://www.urionlinejudge.com.br/judge/" + "en/profile/" + username

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

solved = soup.find_all("span", {"class": "text-bold"})[0].text.strip()

print("Number of problems solved on BeeCrowd: " + solved)
