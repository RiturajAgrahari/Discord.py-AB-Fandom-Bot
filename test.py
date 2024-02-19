import fandom
from bs4 import BeautifulSoup

fandom.set_wiki('arena-breakout')

category = 'Gunsmith'
# category = 'Nightingale Honey '

search = fandom.search(category, results=1)

page_name = search[0][0]
page_no = search[0][1]
print(page_name, page_no)
page = fandom.page(title=page_name)
page2 = fandom.page(pageid=page_no)
print(page == page2)

html_doc = page.html
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
headings = soup.find_all('span', class_='mw-headline')
headings.reverse()
neglect = []

for heading in headings:
    items = heading.find_all_next('div', class_='lightbox-caption')
    print(f"\n---------------{heading.text}--------------\n")
    for i in range(0, len(items)):
        # print(f"{items[i].text}, neglect : {neglect}")
        if items[i].text in neglect:
            break
        else:
            print(f"{i}: {items[i].text}")

        if i == 0:
            neglect.append(items[i].text)

# content = page.content
# print(content)
# section = page.sections
# print(section)
# images = page.images
# print(images)



# print('\n\n\n----------------------------------------------------------------------')
#
# print(f"Title: {content['title']}")
# print(f"Description: {content['content']}")
# print(f"########### INFOBOX ##########")
# infobox = content['infobox'].split('\n')
# print(images[0])
# for i in range(0, len(infobox)):
#     if i < 3:
#         print(infobox[i])
#     else:
#         if i%2 != 1:
#             pass
#         else:
#             print(f"{infobox[i]} : {infobox[i + 1]}")
#
# print('----------------------------------------------------------------------')