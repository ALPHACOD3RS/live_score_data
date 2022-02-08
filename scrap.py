import requests
from bs4 import BeautifulSoup


def news():
    page = requests.get(
        "https://soccerethiopia.net/football/category/news").text
    soup = BeautifulSoup(page, 'lxml')
    datas = soup.find_all('div', class_='entry-grid hgrid')
    allData = []
    id = 0
    for data in datas:
        topicarr = []
        image = data.find('img', itemprop='image').get('src')
        headline = data.find('a', itemprop='url').text
        author = data.find('span', itemprop='name').text
        dataPublished = data.find('time', itemprop='datePublished').text
        allTopics = data.find_all('a', rel='category tag')
        description = data.find('p').text
        description = description.strip("ተጨማሪ")
        for i in allTopics:
            topicarr.append(i.text)
        topic = ", ". join(topicarr)
        allData.append({
            "id": id,
            "image": image,
            "headline": headline,
            "author": author,
            "datePublished": dataPublished,
            "topic": topic,
            "description": description
        })
        id += 1
    return allData
