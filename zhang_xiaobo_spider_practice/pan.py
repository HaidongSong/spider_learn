
#需求：爬取梨视频的视频数据

import requests
import random
from lxml import etree
import os
from multiprocessing.dummy import Pool
headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
}

#原则：县城管吃处理的是阻塞且耗时的操作

#对下述url发起请求解析出视频详情页的url和视频的名称
url = 'https://www.pearvideo.com/category_5'

page_text = requests.get(url = url , headers = headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id = "listvideoListUl"]/li')
urls = []  #存储所有视频的连接and名字
for li in li_list:
   detail_url ='https://www.pearvideo.com/' +  li.xpath('./div/a/@href')[0]
   detail_name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
   #print(detail_url,detail_name)
   #detail_page_text = requests.get(url=detail_url,headers=headers).text
   #从详情页中解析出视频的地址(url)

detail_v_url = ' https://www.pearvideo.com/videoStatus.jsp?'
headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
       "Referer": detail_url
   }
params = {
       'contId': detail_url[-7:],
       'mrd': str(random.random())
   }

response = requests.get(url = detail_v_url, params = params , headers = headers)
page_detail_text = response.json()
   #print(page_detail_text)
   #获取视频url
get_url=page_detail_text['videoInfo']['videos']['srcUrl']
   #print(get_url)
   #获取时间点
systemTime = page_detail_text['systemTime']

#print(systemTime)
   #创建一个用于替换get_url中systemTime的url_part
url_part = 'cont-' + detail_url[-7:]
   #print(url_part)
   #替换get_url中systemTime的url_part形成新的new_url
new_url = get_url.replace(systemTime,url_part)
   #print(new_url)

dic = {
       'name': detail_name,
       'url':new_url
   }
urls.append(dic)

#print(urls)

def get_data(dic):
    url = dic['url']
    name = dic['name']
    #print(url,name)
    print(name,'开始下载...')
    video_data = requests.get(url=url,headers=headers).text

    if not os.path.exists('F:/OneDrive/Workspace/test/mp4'):
        os.mkdir('F:/OneDrive/Workspace/test/mp4')
        path = 'F:/OneDrive/Workspace/test/mp4/' + name
        with open(path,'wb') as fp:
            fp.write(video_data)
        print(name,'下载成功...')

pool = Pool(4)
pool.map(get_data,urls)
pool.close()
pool.join