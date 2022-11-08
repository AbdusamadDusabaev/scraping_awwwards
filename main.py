import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


domain = "https://www.awwwards.com"
headers = {"user-agent": UserAgent().chrome}
index = 0
for page in range(1, 314):
    url = f"https://www.awwwards.com/websites/?page={page}"
    response = requests.get(url=url, headers=headers)
    bs_object = BeautifulSoup(response.content, "lxml")
    sites = bs_object.find(name="ul", class_="grid-sites").find_all(name="li")
    site_urls = [domain + site.div.figure.a["href"] for site in sites]
    for site_url in site_urls:
        index += 1
        with open("links_to_sites_demo.txt", "a", encoding="utf-8") as file:
            file.write(f"{site_url}\n")
        if index == 500:
            break
    if index == 500:
        break
