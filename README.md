# ScrapyProjects

## 目录
- MeiZiTu_1 

---

### MeiZiTu_1 
- 目标网站：meizitu.com
- 运行：运行项目里面的cmdline.py。
- 说明：
    - 直接使用ImagePipeline类：简单但是不灵活。
    - 图片名称是图片下载链接经过SHA1哈希后的值，由scrapy处理。
    - 爬虫流程
        1. 确定要爬取的Items结构：'image_urls'和'images'。  
        'image_urls'存放在网页提取到的图片urls。  
        'images'被填充图片下载成功结束后，图片下载路径、url和校验码等信息。
        2. 爬取下一页：由于目标网站下一页URL格式为'http://meizitu.com/a/more_XXX（数字）.html', 所以我们在此采用URL数字页码+1拼接的形式得到下一页URL。
        3. 结束阶段：使用try来获取max_page，因为最后一页'末页'标签改变了，不用try将匹配不到相应内容导致越界。
        4. 调整：如果无需爬取完全部页数，可更改meizitu_spider.py中'parse'函数if处，详情请看代码。
- 注意：
    - 目标网站下一页的图片URL和首页不一致，需额外添加xpath规则，不然会匹配不到相应图片。
- 效果图

    - full
        ![](https://raw.githubusercontent.com/LZC6244/ScrapyProjects/master/MeiZiTu_1/MeiZiTu/images_demo/1.png)
    - thumbs
        ![](https://raw.githubusercontent.com/LZC6244/ScrapyProjects/master/MeiZiTu_1/MeiZiTu/images_demo/2.png)
    - big
        ![](https://raw.githubusercontent.com/LZC6244/ScrapyProjects/master/MeiZiTu_1/MeiZiTu/images_demo/3.png)
    - small
        ![](https://raw.githubusercontent.com/LZC6244/ScrapyProjects/master/MeiZiTu_1/MeiZiTu/images_demo/4.png)
    
