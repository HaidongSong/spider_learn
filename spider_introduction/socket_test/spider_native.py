from urllib import request
from io import BytesIO
import gzip
import re


# headers = {'User-Agent': 'Mozilla/5.0 3578.98 Safari/537.36'}
# url = Request(url, headers=headers)
# 抓取数据e
# content = urlopen(url,timeout=15).read()
# def getHtml(url):
#         headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
#     page1=urllib.request.Request(url,headers=headers)
#     page=urllib.request.urlopen(page1)
#
#     html=page.read()


class Spider:
    url = 'https://www.douyu.com/g_LOL'
    # url = request('https://www.douyu.com/g_LOL', headers=headers)
    headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                              ' (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')}
    root_pattern = r'<div class="DyListCover-content">([\s\S]*?)2></div>'
    name_pattern = (r'</span><h2 class="DyListCover-user is-template"><svg>'
                    r'<use xlink:href="#icon-user_c95acf8"></use></svg>([\s\S]*?)</h')
    number_pattern = r'</svg>([\s\S]*?)</span>'

    # @staticmethod
    def __fetch_content(self):
        page1 = request.Request(Spider.url, headers=Spider.headers)
        r = request.urlopen(page1)
        # r = request.urlopen(Spider.url)
        html = r.read()
        buff = BytesIO(html)
        f = gzip.GzipFile(fileobj=buff)
        html = f.read().decode('utf-8')
        # html = str(html, encoding='utf8')
        a = 1
        return html

    # @staticmethod
    def __analysis(self, html):
        anchors = []
        root_html = re.findall(Spider.root_pattern, html)
        for htm in root_html:
            root_number = re.findall(Spider.number_pattern, htm)
            root_name = re.findall(Spider.name_pattern, htm)
            anchor = {"name": root_name, "number": root_number}
            anchors.append(anchor)
        # print(anchors)
        return anchors
        # return root_html
        a = 1

    # @staticmethod
    def __refine(self, anchors):
        l = lambda anchor: {'name': anchor['name'][0], 'number': anchor['number'][0]}
        return map(l, anchors)
        a = 1

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__seed, reverse=True)
        return anchors

    # @staticmethod
    def __seed(self, anc):
        for number in anc:
            number = re.findall(r'\d*', anc['number'])
            number = float(number[0])
            if '万' in anc['number']:
                number *= 10000
            return number

    # @classmethod
    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank ' + str(rank + 1) + ':   ' + anchors[rank]['name'] + '-----' + anchors[rank]['number'])

    def go(self):
        html = self.__fetch_content()
        root_html = self.__analysis(html)
        anchors = list(self.__refine(root_html))
        anchors = self.__sort(anchors)
        self.__show(anchors)
        # print(anchors)
        # print(root_html[0])


spider = Spider()
spider.go()
