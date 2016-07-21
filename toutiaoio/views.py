import datetime

from django.shortcuts import render

# Create your views here.
from spider.toutiaoio.main_spider import get_article_by_date


def index(request, year=None, month=None, day=None):
    datas = {}
    print("year", year)
    try:
        datas["year"] = int(year)
        datas["month"] = int(month)
        datas["day"] = int(day)
        pass
    except:
        # print("i am here")
        today = datetime.date.today()
        datas["year"] = today.year
        datas["month"] = today.month
        datas["day"] = today.day
        pass
    try:
        datas["articles"] = get_article_by_date(datas["year"], datas["month"], datas["day"])
        pass
    except:
        datas["articles"] = []
        pass
    datas["articlenums"] = len(datas["articles"])
    upvotenums = 0
    commentnums = 0
    for article in datas["articles"]:
        upvotenums += int(str(article.upvote).strip())
        commentnums += int(str(article.comment).strip())
    datas["upvotenums"] = upvotenums
    datas["commentnums"] = commentnums
    return render(request, 'toutiaoio/toutiaoio.html', datas)
    pass
