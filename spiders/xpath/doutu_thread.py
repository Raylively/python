import requests
import os
from lxml import etree
from urllib import request
import re
import threading
from queue import Queue


class Proceduer(threading.Thread):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
    }

    def __init__(self, page_queue, img_queue ,*args, **kwargs):
        super(Proceduer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.text)
        if not html:
            pass
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            # 获取图片后缀
            suffix = os.path.splitext(img_url)[1]
            alt = img.get('alt')
            # 去除图片名称中的特殊字符
            alt = re.sub(r'\？?\.。，！!\*]', '', alt)
            file_name = alt + suffix
            self.img_queue.put((img_url,file_name))
            # request.urlretrieve(img_url, 'images/' + file_name)

class Consumer(threading.Thread):

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_utl,filename = self.img_queue.get()
            request.urlretrieve(img_utl,'images/'+ filename)
            print(filename+ ' 下载完成！')

def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for i in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % i
        page_queue.put(url)

    for i in range(5):
        t = Proceduer(page_queue,img_queue)
        t.start()
    for i in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()
