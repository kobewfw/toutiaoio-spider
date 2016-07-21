# coding: utf-8
from urllib.parse import urljoin

import bs4


class ToutiaoioParser(object):
    def __init__(self, html_content, root_url):
        self.soup = bs4.BeautifulSoup(html_content, 'html.parser', from_encoding="utf-8")
        self.root_url = root_url

    def parse(self):
        # print(self.soup.prettify())
        reses = self.soup.find_all("div", class_="post")
        print("共 %d 条记录." % len(reses))
        datas = []
        for res in reses:
            try:
                # print(res)
                # print("*" * 50)
                data = {}
                data["title"] = res.find_all("h3", class_="title")[0].find("a").string

                # 点赞
                try:
                    data["upvote"] = res.find("div", class_="upvote").find("a").find("span").string
                    data["upvote"] = str(data["upvote"]).strip()
                    # print(data["upvote"])
                    pass
                except:
                    print("解析 %s 时无法解析 %s" % (data["title"], "upvote"))
                    pass

                try:
                    data["url"] = res.find_all("h3", class_="title")[0].find("a").get("href")
                    pass
                except:
                    print("解析 %s 时无法解析 %s" % (data["title"], "url"))
                    pass

                try:
                    data["source"] = str(list(res.find("div", class_="meta").children)[0]).strip()
                    pass
                except:
                    print("解析 %s 时无法解析 %s" % (data["title"], "source"))
                    pass

                try:
                    # data["comment"] = str(res.find_all("i")[0]).strip()
                    data["comment"] = str(list(res.find("div", class_="meta").find("span").children)[2]).strip()
                    # print(data["comment"])
                    pass
                except:
                    print("解析 %s 时无法解析 %s" % (data["title"], "comment"))
                    pass

                try:
                    data["username"] = res.find("div", class_="info").find("h4").string
                    pass
                except:
                    print("解析 %s 时无法解析 %s" % (data["title"], "username"))
                    pass

                try:
                    data["userurl"] = urljoin(self.root_url, str(res.find("div", class_="info").find("a")["href"]))
                    pass
                except:
                    print("解析 %s 时无法解析 %s" % (data["title"], "userurl"))
                    pass

                try:
                    data["subjectname"] = res.find("div", class_="subject-name").find("a").string
                    pass
                except:
                    print("解析 %s 时无法解析 %s" % (data["title"], "subjectname"))
                    pass

                try:
                    data["subjecturl"] = urljoin(self.root_url,
                                                 res.find("div", class_="subject-name").find("a").get("href"))
                    pass
                except:
                    print("解析 %s 时无法解析 %s" % (data["title"], "subjecturl"))
                    pass

                try:
                    data["userpic"] = res.find("div", class_="info").find("img").get("src")
                    pass
                except:
                    print("解析 %s 时无法解析 %s" % (data["title"], "userpic"))
                    pass
            except Exception as e:
                print("解析页面 %s 失败." % (self.root_url, ))
                import traceback
                traceback.print_exc()
            else:
                # print("解析了一条记录: %s" % data["title"])
                datas.append(data)
        return datas
        pass
    pass



