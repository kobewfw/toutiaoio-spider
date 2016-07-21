# coding: utf-8
import urllib
import urllib.request
import urllib.response


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        data=None
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
        req = urllib.request.Request(url, data, headers)
        res = urllib.request.urlopen(req, timeout=5)
        if res.getcode() != 200:
            print("下载页面 %s 失败." % url)
            return None
        print("下载页面 %s 成功." % url)
        return res.read()
        pass
    pass


if __name__=="__main__":
    downloader = HtmlDownloader()
    print(str(downloader.download("http://toutiao.io/"), encoding='utf8'))
    pass
