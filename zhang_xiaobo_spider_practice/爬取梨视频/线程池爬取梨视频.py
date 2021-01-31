import json
import requests
from multiprocessing.dummy import Pool
from lxml import etree
import random
import re
import os
import logging

import log


headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }


def myparse():
    global headers
    urls = []
    res = requests.get(url='https://www.pearvideo.com/category_8', headers=headers)
    if res.status_code == 200:
        logging.info('抓取成功。。。开始解析数据。。。')
        tree = etree.HTML(res.text)
        ul = tree.xpath('//div[@id="listvideoList"]//ul[@id="listvideoListUl"]/li')
        for li in ul:
            video_url = li.xpath('.//div[@class="vervideo-bd"]/a/@href')[0]
            name = li.xpath('.//div[@class="vervideo-title"]/text()')[0]
            regex_str = r'\d.*'
            regex_str_compile = re.compile(str(regex_str))
            content_id = regex_str_compile.findall(video_url)[0]
            params = {
                'contId': content_id,
                'mrd': str(random.random())
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'Host': 'www.pearvideo.com',
                'Referer': 'https://www.pearvideo.com' + video_url
            }

            video_detial = requests.get('https://www.pearvideo.com/videoStatus.jsp?', params=params, headers=headers)
            if video_detial.status_code == 200:
                video_detial_content = video_detial.text
                video_content_dict = json.loads(video_detial_content)
                video_download_url = video_content_dict.get('videoInfo').get('videos').get('srcUrl')
                systemTime = video_content_dict.get('systemTime')
                video_download_url = video_download_url.replace(systemTime, 'cont-'+headers.get('Referer')[-7:])
                mp4_info = {
                    "name": name,
                    'url': video_download_url
                }
                urls.append(mp4_info)
            else:
                logging.error('包含视频下载地址的json文件获取失败，请检查。。。')
    else:
        logging.error('数据获取失败，请检出url')
    return urls, headers


def download(video_info):
    path = os.path.dirname(os.path.abspath(__file__)) + '/videos'
    video_content = requests.get(url=video_info.get('url'))
    if video_content.status_code == 200:
        logging.info(f"正在下载视频: {video_info.get('name')}。。。")
        video_content_byte = video_content.content
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path+'/'+video_info["name"]+'.mp4', 'wb') as fp:
            fp.write(video_content_byte)
        logging.info(f"下载Ok!!! {video_info.get('name')} ")
    else:
        logging.error('视频下载出错！！！')


if __name__ == '__main__':
    log.startlogging()
    urls_infos, headers = myparse()
    pool = Pool(4)
    pool.map(download, urls_infos)
    pool.close()
    pool.join()
