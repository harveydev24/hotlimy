from bs4 import BeautifulSoup
import requests


def fmkorea_crawl(targets):
    FMKOREA_URL = "https://www.fmkorea.com"
    response = requests.get(FMKOREA_URL + "/hotdeal")

    result = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        last_idx = 20

        for i in range(1, last_idx+1):
            selected = soup.select_one(
                f"#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li:nth-child({i}) > div > h3 > a")
            payload = selected['href']
            title = selected.get_text().strip()

            for target in targets:
                if target in title:
                    result.append(title + " " + FMKOREA_URL + payload)

    return result
