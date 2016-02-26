# ScrapyTwitter
Crawling twitter info Using Scrapy+Splash

1.安装docker。mac 不能直接操作docker demaon, 要装 boot2docker
command run: docker run -it -p 8050:8050 scrapinghub/splash --max-timeout 3600
查看ip: docker-machine ls
然后打开浏览器 输入 Ip:8050,看到splash 网页，就可以运行spider。

2. 在setting 文件之中，添加配置，才能在scarpy中运行，splash爬动态网页
SPLASH_URL = 'http://你的ip:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapyjs.SplashMiddleware': 725,
}
DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapyjs.SplashAwareFSCacheStorage'



3. command run:
cd 到最外层文件下
scrapy   crawl spider文件名 -o out.json -t json
