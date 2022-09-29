'''
Author: MJ.XU
Date: 2022-07-25 22:47:52
LastEditTime: 2022-09-10 21:43:42
LastEditors: MJ.XU
Description: 
Personal URL: https://www.squirrelled.cn/
'''
from unicodedata import name
import url_test
import threading
import time


def single_thread():
    for url in url_test.urls:
        url_test.craw(url)
    print("Single is over")


def multi_thread():
    threads = []
    for url in url_test.urls:
        threads.append(threading.Thread(target=url_test.craw, args=(url, )))

    for thread in threads:
        thread.start()

    for thread in threads:  # 等待thread结束
        thread.join()
    print("Multi is over")


if __name__ == "__main__":
    start = time.time()
    single_thread()

    end = time.time()
    print("Single cost seconds are:", end - start)

    start = time.time()
    multi_thread()
    end = time.time()
    print("Multi cost seconds are:", end - start)
