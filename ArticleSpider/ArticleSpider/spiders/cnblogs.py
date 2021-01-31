from urllib import parse
import json
import re

import scrapy
from scrapy import Request
from ArticleSpider.items import CnblogsAriticleSpiderItem
# from ArticleSpider.ArticleSpider.items import CnblogsAriticleSpiderItem
from ArticleSpider.util.hash import get_md5


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']

    def parse(self, response):
        post_node = response.xpath('//div[@class="news_block"]//div[@class="content"]')
        for i in post_node:
            detial_url = i.xpath('./h2[@class="news_entry"]/a/@href').extract_first('')
            image_url = i.xpath('./div[@class="entry_summary"]/a/img/@src').extract_first('')
            if image_url:
                if 'http' not in image_url:
                    image_url = "https:" + image_url

            yield (Request(parse.urljoin(response.url, detial_url), meta={"front_image_url": image_url},
                           callback=self.parse_detial))
        # next_url1 = response.xpath('//*[@class="pager"]/a[contains(text(), "Next >")]/@href').extract_first('')
        next_url = response.xpath('//*[@class="pager"]/a[contains(text(), "Next >")]/@href').extract_first('')
        # url_test = parse.urljoin(response.url, next_url)
        yield Request(parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detial(self, response):
        article_item = CnblogsAriticleSpiderItem()
        title = response.xpath('//*[@id="news_title"]/a/text()').extract_first('')
        create_time_str = response.css("#news_info span.time::text").extract_first('')
        origin_url = re.compile(r'.*?(\d+.*)')
        # create_time_list = origin_url.findall(create_time_str)
        # create_time = create_time_list[0]
        create_time_str = origin_url.match(create_time_str)
        if create_time_str:
            create_time = create_time_str.group(1)
        else:
            create_time = ''
        # news_poster = response.css("#news_info span.news_poster a::text").extract_first()
        news_poster = response.xpath("//*[@id='news_info']/span[@class='news_poster']/a/text()").extract_first()
        content = response.css('#news_content').extract_first()
        tag_list = response.css('#news_more_info .news_tags a::text').extract()
        tags = ''.join(tag_list)
        content_id = re.findall(r'\d+', response.url)[0]
        url_hash = get_md5(response.url)
        if content_id:
            article_item['title'] = title
            article_item['create_time'] = create_time
            article_item['news_poster'] = news_poster
            article_item['content'] = content
            article_item['tags'] = tags
            article_item['url'] = response.url
            article_item['url_hash'] = url_hash
            # article_item['front_image_url'] = ([] if not response.meta.get('front_image_url', '')
            #                                    else [response.meta.get('front_image_url', '')])
            if response.meta.get('front_image_url', ''):
                article_item['front_image_url'] = [response.meta.get('front_image_url', '')]
            else:
                article_item['front_image_url'] = []
            yield Request(parse.urljoin(response.url, '/NewsAjax/GetAjaxNewsInfo?contentId={}'.format(content_id)),
                          meta={'article_item': article_item}, callback=self.detial_data)

    def detial_data(self, response):
        article_item = response.meta.get('article_item', '')
        if response.text:
            text = response.text
            text_serialize = json.loads(text)
            if text_serialize:
                comment_nums = text_serialize.get('CommentCount', 0)
                total_view = text_serialize.get('TotalView', 0)
                digging_count = text_serialize.get('DiggCount', 0)
                article_item['comment_nums'] = comment_nums
                article_item['total_view'] = total_view
                article_item['digging_count'] = digging_count

                yield article_item
