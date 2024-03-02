import fandom
from bs4 import BeautifulSoup
from typing import Literal, Union

fandom.set_wiki('arena-breakout')

DATA = {}
categories = ['Provisions', 'Gear']
# categories = ['Medicine', 'Provisions', 'Gear', 'Gunsmith']

def get_category():
    for category in categories:
        search = fandom.search(category, results=1)

        page_name = search[0][0]
        page_no = search[0][1]
        # print(page_name, page_no)
        page = fandom.page(title=page_name)
        page2 = fandom.page(pageid=page_no)
        # print(page == page2)

        html_doc = page.html
        soup = BeautifulSoup(html_doc, 'html.parser')
        # print(soup.prettify())
        headings = soup.find_all('span', class_='mw-headline')
        headings.reverse()
        neglect = []

        for heading in headings:
            detail = []
            items = heading.find_all_next('div', class_='lightbox-caption')
            # print(f"\n---------------{heading.text}--------------\n")
            for i in range(0, len(items)):
                # print(f"{items[i].text}, neglect : {neglect}")
                if items[i].text in neglect:
                    break
                else:
                    detail.append(items[i].text)
                    # print(f"{i}: {items[i].text}")

                if i == 0:
                    neglect.append(items[i].text)

            if detail:
                Tup = tuple(detail)
                DATA[f'{heading.text}'] = Tup


    # print(f"-----------------------DATA----------------------")
    # for keys, value in DATA.items():
    #     print(f"{keys}: {value}\n")

get_category()


