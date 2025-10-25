import requests
from lxml import html
from urllib.parse import urljoin
import time
import csv
import re
#数据清洗
def test_clean(text):
    result = re.sub(r'\s+', '',text )
    result = re.sub(r'[a-zA-Z]', '', result)
    result = re.sub(r'''[^\u4e00-\u9fa50-9，。！？；："'‘'“”（）《》【】]''','',result)
    result = re.sub(r'[0-9]{5,}','',result)
    result = re.findall(r'正文.*加入收藏',result)
    result = list_to_str(result)
    patterns_to_remove = [
        '正文',
        '加入收藏', 
        '字体：大中小分享到：',
        '发布时间：'
        ]
    for pattern in patterns_to_remove:
        result = re.sub(pattern, '', result)

    return result




page = 205
final_page = 205

all_hrefs = []
all_titles = []
#翻页
while page <= final_page:
    url = f'https://jwch.fzu.edu.cn/jxtz/{page}.htm'
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
    
    web_info = requests.get(href)
    tree1 = html.fromstring(web_info.content)

    #爬取数据
    text_list = tree1.xpath('//text()')
    title = tree1.xpath('/html/body/div[1]/div[2]/div[2]/form/div/div[1]/div/div[1]/h4/text()')
    department = tree1.xpath('/html/body/div[1]/div[2]/div[1]/p/a[3]/text()')
    print(title)
    print(department)
    #print(list_to_str(text_list))

    
    result = test_clean(list_to_str(text_list))
    print(result)

    text = f'出处：{department} {result}'
    print(text)
    i += 1
    with open('data.csv','a',newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(text)


    #获取附件
    file_urls = tree1.xpath('/html/body/div[1]/div[2]/div[2]/form/div/div[1]/div/ul//li/a/@href')
    file_names = tree1.xpath('/html/body/div[1]/div[2]/div[2]/form/div/div[1]/div/ul//li/a/text()')
    #print(files)
    #print(file_name)
    
    if file_urls:
        i = 0
        for file_url in file_urls:
            with open(f'file/{file_names[i]}','wb') as f:
                file_url = urljoin('https://jwch.fzu.edu.cn',file_url)
                file = requests.get(file_url)
                f.write(file.content)
    time.sleep(1)





