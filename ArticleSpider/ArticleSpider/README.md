# Question

1. re.findall(s,x)[0]会报错
   rem.match(),就可以
2. response.css('#new_content').extract()[0]会报错 

    - extract_first()就可以
    - 返回的html结构中有的img中的url缺失部分数据，源码是没问题的
3. response.xpath()获取到的url有的有‘http://’,有的没有

   
4. response.css('#news_content'')
参考 front_image_url