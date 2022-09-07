from bs4 import BeautifulSoup
import requests


def ppomppu_crawl(targets):
    PPOMPPU_URL = "https://www.ppomppu.co.kr/zboard"
    response = requests.get(PPOMPPU_URL+"/zboard.php?id=ppomppu")

    result = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        selected = soup.select("div > a > font")

        for item in selected:
            title = item.get_text().strip()

            for target in targets:
                if target in title:
                    payload = item.parent['href']
                    result.append(title + " " + PPOMPPU_URL + '/' + payload)

    return result
