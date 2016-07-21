# coding: utf-8
from spider.public.html_downloader import HtmlDownloader
from spider.public.url_manager import UrlManager
from spider.toutiaoio.toutiaoio_parser import ToutiaoioParser
from spider.toutiaoio.toutiaoio_outputer import Outputer
from toutiaoio.models import ToutiaoItem

ROOT_URL = "http://toutiao.io/"


class ToutiaoioSpider(object):
    # TODO
    def __init__(self, root_url=ROOT_URL, date=""):
        self.downloader = HtmlDownloader()
        self.urls = UrlManager
        self.parser = ToutiaoioParser(self.downloader.download(root_url), root_url)
        self.outputer = Outputer()

    def run(self):
        datas = self.parser.parse()
        self.outputer.save(datas)
        pass

    def get(self):
        datas = self.parser.parse()
        reses = []
        for data in datas:
            try:
                item = ToutiaoItem(title=data.get("title"), url=data.get("url"), source=data.get("source"),
                                   comment=data.get("comment"), username=data.get("username"),
                                   userurl=data.get("userurl"), subjectname=data.get("subjectname"),
                                   subjecturl=data.get("subjecturl"), upvote=data.get("upvote"))
                reses.append(item)
            except Exception as e:
                import traceback
                traceback.print_exc()
                print("格式化结果时出现了一个错误")
                pass
            pass
        return reses
    pass


def get_article_by_date(year, month, day):
    _root_url = "http://toutiao.io/prev/" + str(year) + "-" + str(month) + "-" + str(day)
    _spider = ToutiaoioSpider(_root_url)
    # print(_spider.get())
    return _spider.get()
    pass

if __name__ == "__main__":
    get_article_by_date(2016, 7, 19)
    # spider = ToutiaoioSpider("http://toutiao.io/prev/2016-07-17")
    # spider.run()
    pass
