# -*- coding:utf-8 -*-
'''您可(sha)爱(bi)的图(wang)灵(tong)机在半夜才重写完这个程序，犯蠢可以说是从头到尾了。哎哟，为什么这么菜啊？'''
'''本程序可以用于分析一段文本的情感倾向，并给出positive、mid、negative三种判断，并给出置信度'''

from aip import AipNlp
import numpy
import time
import os
import glob
from bs4 import UnicodeDammit
import chardet
import re

'''
here is the key of the API
'''
APP_ID = '11297825'
API_Key = 'NTDqXD9NglB22MGg3RRbG9WW'
Secret_Key = 'LKmODb2nvtyegvgqx3qp31Gh1TtngSyK'

client = AipNlp(APP_ID, API_Key, Secret_Key)  # init the client

switch = {'0': 'negative', '1': 'mid', '2': 'positive'}  # 一个简单switch功能块
# file = open('铅球.txt', 'rt', encoding="utf-8")

# 显示感情分析结果
def showAns(text):
    tmpClient = client.sentimentClassify(text)
    print('class of the text: ', switch[str(tmpClient['items'][0]['sentiment'])])
    print('the confidence of the ans: ', tmpClient['items'][0]['confidence'])
    print('positive_prob: ', tmpClient['items'][0]['positive_prob'])
    print('negative_prob: ', tmpClient['items'][0]['negative_prob'])
    print('--------------------------------------------------------------' + '\n')

 # 请求结果并分析后格式化返回
def saveAns(text, data):
    # print(UnicodeDammit(text).original_encoding)
    # text = filter_emoji(text)
    errorFlag = 0
    '''
    这个地方不得不说是我傻逼了，我压根忘了可以try，引以为戒。
    根据是否发生过exception，来将errorFlag置位，后续用作判断
    但同样需要注意的是，try块会极大的降低效率，这个问题过两天再说。
    '''
    try:
        tmpClient = client.sentimentClassify(text)
        print(tmpClient)
        if 'items' in tmpClient:
            data.append(text)
            data.append(switch[str(tmpClient['items'][0]['sentiment'])])
            data.append(str(tmpClient['items'][0]['confidence']))
    except UnicodeEncodeError as e:
        print("error", e)
        errorFlag = 1
    return data, errorFlag

# 消除文本中的emoji
def filter_emoji(desstr, restr=u''):
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)


if __name__ == '__main__':
    start_time = time.time()
    '''
    text1 = '男孩子呀你要明白,女孩子的撒娇、女孩子的任性、女孩子的小脾气都是在告诉你,快抱抱我'
    showAns(text1)
    text2 = '谈了个恋爱，心累，突然之间心好疼'
    showAns(text2)
    '''
    data = []
    dataMat = []
    os.chdir('data\摇滚\\')   # 定位目录
    files = glob.glob('*.txt')  # here   files  is   the   name  of  the  txt
    print(files)
    for eachFile in files:
        print("now is: " + eachFile)
        file = open('C:\\Users\moyuan\PycharmProjects\\test\data\\摇滚\\' + eachFile, 'r', encoding='utf-8')
        # 此处相对定位有小问题，换用绝对定位

        dataMat = []
        lineNo = 0
        for line in file.readlines():
            if lineNo < 50:   # 用于控制提取多少条评论，如果要全部读取，则删除整个if结构，将if-stmt向上一级
                fileWrite = open('C:\\Users\moyuan\PycharmProjects\\test\data\\yg\\' + 'ans_' + eachFile, 'a',
                                 encoding='utf-8')
                print('Now the lineNo is: ' + str(lineNo))
                # line.encode('utf-8')
                error = 0
                data = []
                line = line.strip()
                # line.encode('utf-8').decode('utf-8').encode('gbk', 'ignore')
                data, error = saveAns(line, data)
                dataMat.append(data)
                lineNo += 1
                '''此处利用了try的判据，根据判据来决定是否写数据。若不执行判断，则数组越界'''
                if error == 0:
                    print(data)
                    fileWrite.write(data[0] + '\t' + data[1] + '\t' + data[2] + '\n')
                '''
                for each in data:
                    print(each)
                    fileWrite.write(each + '\n')
                '''
                fileWrite.close()
            else:
                break

        '''
        for eachAns in dataMat:
            fileWrite.write(eachAns[0] + '\t' + eachAns[1] + '\t' + eachAns[2] + '\n')
        '''
        file.close()
        fileWrite.close()

    end_time = time.time()
    print("END")
    print("用时%f秒" % (end_time - start_time))

    '''
    从此处开始是之前的版本，可以直接略过
    data = []
    for line in file.readlines():
        curline = line.strip().split(' ')
        curline = list(curline)
        data.append(curline)

    dataMat = numpy.array(data)
    ansMat = []
    ans = []
    for rows in dataMat:
        ans = []
        json_ans = client.sentimentClassify(rows[5])
        ans.append(rows[5])
        ans.append(switch[str(json_ans['items'][0]['sentiment'])])
        ans.append(json_ans['items'][0]['confidence'])
        ansMat.append(ans)

    file = open('nlp_ans.txt', 'w', encoding='utf-8')
    for each in ansMat:
        file.write(each[0] + '\t' + each[1] + '\t' + str(each[2]) + '\n')

    end_time = time.time()
    print("END")
    print("用时%f秒" % (end_time - start_time))
    '''


