
import requests
import os
from lxml import etree
from urllib import request
import re

def parse_page(url):
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
    }
    response = requests.get(url,headers=headers)
    html = etree.HTML(response.text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        # 获取图片后缀
        suffix = os.path.splitext(img_url)[1]
        alt = img.get('alt')
        # 去除图片名称中的特殊字符
        alt = re.sub(r'\？?\.。，！!]','',alt)
        file_name = alt + suffix
        request.urlretrieve(img_url,'images/' + file_name)


def main():
    for i in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % i
        parse_page(url)

if __name__ == '__main__':
    main()
