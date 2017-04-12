# 使用 Scrapy 爬取 当当网 特产信息
数据包括: "价格"、"名称"、"连接"、"评论次数" 使用说明：
首先克隆服务代码：
```
$ git clone https://github.com/slzcc/Scrapy-DangDang.git
```
进入项目安装 scrapy 模块，如果已经存在请忽略
```
$ cd Scrapy-DangDang
$ pip install -r Module.txt
```
执行 `main.py` 获取数据
```
$ python autopjt/spiders/main.py
$ cat mydata.json
```
获取到的数据展示：
![Json-list set up](https://github.com/slzcc/Scrapy-DangDang/blob/master/template/json-list.png)
