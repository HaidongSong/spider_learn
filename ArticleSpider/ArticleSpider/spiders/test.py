# import scrapy
#
# html = scrapy.Request('https://news.cnblogs.com/n/685416/')
# print(html)
# print(html.text)
import requests

res = requests.get('https://video.pearvideo.com/mp4/adshort/20210119/cont-1716976-15579643_adpkg-ad_hd.mp4')
p = res.content
print(p)