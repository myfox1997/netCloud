# coding: utf-8
from aip import AipNlp
import numpy
import time

'''
here is the key of the API
'''
APP_ID = '11297825'
API_Key = 'NTDqXD9NglB22MGg3RRbG9WW'
Secret_Key = 'LKmODb2nvtyegvgqx3qp31Gh1TtngSyK'

client = AipNlp(APP_ID, API_Key, Secret_Key)

# 评论标签函数，当 1< Option < 14的时候用特殊标签
def showCommentTag(tagText, Options):
    """ 如果有可选参数 """
    if 1 <= Options < 14:
        options = {}
        options["type"] = Options
        tag_json = client.commentTag(tagText, options)
    else:
        tag_json = client.commentTag(tagText)
    print(tag_json)

def showSentiment(text):
    sentiment = client.sentimentClassify(text)
    print(sentiment)

def lexer(text):
    lexer = client.lexer(text)
    print(lexer)

if __name__ == '__main__':
    # text = '今天的天气真的是变化无常'
    # showCommentTag(text)
    # showSentiment(text)
    # lexer(text)
    # text = "三星电脑电池不给力"
    text = "苹果手机的电池不好"
    """ 带参数调用评论观点抽取 """
    # showCommentTag(text, 13)
    title = '喜欢你'
    content = '''从小到大最幸运的事就是遇见你了.茫茫人海中同年同月同日生的咱俩相遇在这所大学 这本身就是可遇不可求的缘分阿.纳米拉 让我一直陪在你身边吧.忐忑给你,情书给你,
不眠的夜给你,
雪糕的第一口给你,
一腔孤勇和余生60年全部都给你'''
    title1 = '抖音来的'
    content1 = '抖友来报道[憨笑]'
    ans = client.topic(title1, content1)
    print(ans)

