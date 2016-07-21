# coding: utf-8
# 使用 Django 模型实现数据存储
import os
import sys

pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '../..')))

# 如果没有设置 DJANGO_SETTINGS_MODULE, 则设置
if os.environ.get("DJANGO_SETTINGS_MODULE") is None:
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wfw.settings")
    django.setup()
# end
from toutiaoio.models import ToutiaoItem

class Outputer(object):

    @staticmethod
    def save(datas, date=""):
        print("保存 %d 个" % len(datas))
        # 删除保存的相同日期内容
        for item in ToutiaoItem.objects.all():
            if date == item.date:
                item.delete()

        for data in datas:
            try:
                item = ToutiaoItem(title=data.get("title"), url=data.get("url"), source=data.get("source"),
                                   comment=data.get("comment"), username=data.get("username"),
                                   userurl=data.get("userurl"), subjectname=data.get("subjectname"),
                                   subjecturl=data.get("subjecturl"), upvote=data.get("upvote"), date=date)
                item.save()
            except Exception as e:
                import traceback
                traceback.print_exc()
                print("保存结果时出现了一个错误")
                pass
            pass
    pass
