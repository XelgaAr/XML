import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.pravda.com.ua/rss/view_news/")
# # print(response.text)
#
# bs = BeautifulSoup(response.text, "xml")
# # print(bs.title)
#
# for one_item in bs.find_all("item"):
#     title = one_item.find("title").text
#     # print(one_item)
#     # print(one_item.encode("windows-1251").decode("utf-8", 'ignore'))
#     link = one_item.find("link").text
#     pub_data = one_item.find("pubDate").text
#     user_data = {"title":title,  "link":link, "pub_data": pub_data}
#     print(user_data)


response = requests.get("https://scipost.org/atom/publications/comp-ai")
bs = BeautifulSoup(response.text, "xml")


for one_item in bs.find_all("entry"):
    title = one_item.find("title").text
    # print(one_item)
    # print(one_item.encode("windows-1251").decode("utf-8", 'ignore'))
    link = one_item.find("link").get("href")
    summary = one_item.find("summary").text
    user_parse = {"title": title,  "link": link, "summary": summary}
    print(user_parse)