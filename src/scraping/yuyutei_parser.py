from bs4 import BeautifulSoup as BS

# Go to website
# url = requests.get("https://yuyu-tei.jp/sell/poc/s/m03", headers=headers, timeout = 10 )
# print(url.status_code)

def yuyutei_parser(url_content):

    soup = BS(url_content, "html.parser")
    cards = soup.find_all("div", class_="col-md")
    card_list = []

    for card in cards:
        card_dict = {}
        picture = card.find("div", class_="position-relative product-img")
        price_tag = card.find("strong")

        if picture and picture.find("img"):
            img_tag = picture.find("img")
            card_info = img_tag["alt"]
            number = card_info.split(" ")[0]
            rarity = card_info.split(" ")[1]
            name = card_info.split(" ")[-1]
        else:
            card_info = None
            number = None
            rarity = None
            name = None

        if price_tag:
            price = price_tag.text.strip()
        else:
            price = None

        card_dict['Number'] = number
        card_dict['Rarity'] = rarity
        card_dict['Name'] = name
        card_dict['Price'] = price

        card_list.append(card_dict)

    return card_list
