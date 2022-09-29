'''
Author: MJ.XU
Date: 2022-07-26 15:38:43
LastEditTime: 2022-08-05 19:07:46
LastEditors: MJ.XU
Description: 
Personal URL: https://www.squirrelled.cn/
'''
import queue
import url_test
import time
import random
import threading

# 生产者


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = url_test.craw(url)
        html_queue.put(html)
        print(threading.current_thread().name + f" craw {url}",
              "url_queue.size=", url_queue.qsize())
        time.sleep(random.randint(1, 2))


# 消费者
def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = url_test.parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name + " results.size", len(results),
              "html_queue.size=", html_queue.qsize())
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in url_test.urls:
        url_queue.put(url)

    for idx in range(3):
        t = threading.Thread(target=do_craw,
                             args=(url_queue, html_queue),
                             name=f"craw{idx}")
        t.start()

    fout = open("02.data.txt", "w")
    for idx in range(2):
        t = threading.Thread(target=do_parse,
                             args=(html_queue, fout),
                             name=f"parse{idx}")
        t.start()
