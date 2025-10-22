import requests
from lxml import html
from urllib.parse import urljoin
import time
import csv
    

page = 1
final_page = 1

all_hrefs = []
all_titles = []
#翻页
while page <= final_page:
    url = f'https://jwch.fzu.edu.cn/zhzx/{page}.htm'
    web = requests.get(url)
    tree = html.fromstring(web.content)
    hrefs = tree.xpath('//ul[@class="list-gl"]/*/a/@href')
    titles = tree.xpath('//ul[@class="list-gl"]/*/a/@title')
    all_hrefs += hrefs
    all_titles += titles
    time.sleep(1)
    page += 1

#将列表中字符串合成一整串字符串
def list_to_str(list):
    strs = ''
    for str in list:
        strs += str
    return strs

#补全网址
all_full_hrefs = []
for href in all_hrefs:
    full_href = urljoin(url,href)
    all_full_hrefs.append(full_href)
    
#读取各个网站中文字信息，并存入csv文件
i = 0
for href in all_full_hrefs:
    #print(href)
    web_info = requests.get(href)
    tree1 = html.fromstring(web_info.content)
    text_list = tree1.xpath('//*[@id="vsb_content"]/div/p/span/text()')
    #print(list_to_str(text_list))
    text = f'《{all_titles[i]}》{list_to_str(text_list)}'
    i += 1
    with open('data.csv','a',newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(text)
    time.sleep(1)






