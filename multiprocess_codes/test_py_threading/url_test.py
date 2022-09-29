'''
Author: MJ.XU
Date: 2022-07-25 22:34:03
LastEditTime: 2022-07-26 16:07:42
LastEditors: MJ.XU
Description: 
Personal URL: https://www.squirrelled.cn/
'''
from bs4 import BeautifulSoup
import requests

urls = [f"https://www.cnblogs.com/#p{page}" for page in range(1, 50)]


# print(urls)
# def craw(url):  # 应该使用单个page
#     r = requests.get(url)
#     print(url, len(r.text))


def craw(url):  # 生产者
    r_text = requests.get(url)
    return r_text.text


def parse(html):  # 消费者
    # class="post-item-title"
    soup = BeautifulSoup(html,"html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]


# if __name__ == "__main__":
#     # result=parse(craw_text(cnblogs_urls[0]))
#     # print (result)
#     for result in parse(craw_text(cnblogs_urls[0])):
#         print(result)
## 测试单个craw函数
# craw(urls[0])
