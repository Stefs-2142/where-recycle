from bs4 import BeautifulSoup
import requests


URL = 'https://recyclemap.ru/index.php?id=1440'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.123 Safari/537.36'}


location_id = 23518


def get_html(url, params=None):
    return requests.get(URL, headers=HEADERS)


def get_content(html):
    location_type = []
    soup = BeautifulSoup(html, 'html.parser')

    # Сохраняю в файл, чтобы было проще ковыряться
    # with open("output1.html", "w") as file:
    #     file.write(str(soup))

    # NAME
    location_name = soup.find('div', class_="point_title").get_text()

    # Блок с информацией о локации
    location_data = soup.find_all('div', attrs={"class": "slimScrollDiv", "class": "panel body", "class": "panel_body_wrap"})[1]

    # ADDRESS
    location_description = location_data.find_all('div', attrs={"class": "point_address"})

    # INFO
    location_info = location_data.find_all("div", attrs={"class": "spoiler_inside"})

    # TYPE
    location_types = location_data.find_all("div", attrs={"class": "point_fractions trash_type sm_trash_type"})
    for a in location_types[0].find_all("span"):
        location_type.append(a.attrs["data-tooltip"])

    # IMAGES
    image_url = []
    images = location_data.find_all('a', attrs={'class': 'popup_image'})
    for image in images:
        image_url.append(image.attrs['href'])

    # WORKING HOURS
    working_hours = {}
    time_scheme = location_data.find_all('table', attrs={'class': 'time_schem'})

    if time_scheme:
        for i in range(7):
            working_hours[time_scheme[0].find_all('th')[i].get_text()] = time_scheme[0].find_all('td')[i].get_text(separator="-")
    else:
        hours = location_data.find_all('div', attrs={'class': 'point_spoiler'})[1]
        hours = hours.find_all('a', attrs={'class': 'ico1'})
        working_hours['Время работы'] = hours

    print("------------------------------------")
    print("TITLE:", location_name)
    print("IMAGE", image_url)
    print("WORKING HOURS:", working_hours)
    print("ID:", location_data.attrs['data-id'])
    print("COORDINATES:", location_data.attrs['data-lat'], location_data.attrs['data-lng'])
    print("TYPE", location_type)
    print("ADDRESS:", location_description[0].get_text(strip=True))
    print("INFO:", location_info[0].get_text(strip=True))


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
