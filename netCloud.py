# -*-coding:utf-8-*-

'''
这个程序160行，岂不是美滋滋，算是勉强凑够行数了吧
程序会生成两个文件，一个名为「歌名_src」， 另一个为「歌名_res」
前者为返回的源数据，包含所有的返回信息
后者为经过解析的数据，格式为：评论 + "\t" + 赞数     该文件中每个评论按行排放
'''

import os
import time
import json
import base64
import random

import requests

import codecs
from Crypto.Cipher import AES
songName = "data/电子/Trip"
songID = "36492599"
# 先随机生成一个secKey，长度为16。
# 用该key初始化一个AES模块，对text文本进行两次加密（encText），然后在进行一次rsa加密，得到encSecKey
class CommentCrawl(object):
    '''评论的API封装成一个类，直接传入评论的API，再调用函数get_song_comment()和get_album_comment()即可分别获取歌曲和专辑的评论信息 '''
    def __init__(self, comment_url):
        self.comment_url = comment_url
        self.headers = {
            "Referer": "http://music.163.com/song?id=551816010",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
        }



    # 生成长度为16的随机字符串作为密钥secKey
    def createSecretKey(self, size):
        return (''.join(map(lambda xx: (hex(ord(xx))[2:]), str(os.urandom(size)))))[0:16]

    # 进行aes加密
    def aesEncrypt(self, text, secKey):
        pad = 16 - len(text) % 16
        #print("leix")
        #print(type(text))
        #print(type(pad * chr(pad)))
        if isinstance(text, bytes):        # if the text's type is byte, translate it to txt with utf-8
            #print("type(text)=='bytes'")
            text = text.decode('utf-8')
        text = text + str(pad * chr(pad))       # make the length of text is the multiple of 16
        encryptor = AES.new(secKey, AES.MODE_CBC, '0102030405060708')  # use the iv=0102030405060708 to initial the AES

        ciphertext = encryptor.encrypt(text)   # encrypt the text
        ciphertext = base64.b64encode(ciphertext)  # use the base64 to encode the text
        return ciphertext

    # 进行rsa加密
    def rsaEncrypt(self, text, pubKey, modulus):
        text = text[::-1]
        # rs = int(text.encode('hex'), 16) ** int(pubKey, 16) % int(modulus, 16)
        rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
        return format(rs, 'x').zfill(256)

    # 将明文text进行两次aes加密获得密文encText，因为secKey是在客户端上生成的，所以还需要对其进行RSA加密再传给服务端
    def encrypted_request(self, text):
        # here is the params of the headers
        modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        nonce = '0CoJUm6Qyw8W8jud'
        pubKey = '010001'
        text = json.dumps(text)
        secKey = self.createSecretKey(16)
        encText = self.aesEncrypt(self.aesEncrypt(text, nonce), secKey)
        encSecKey = self.rsaEncrypt(secKey, pubKey, modulus)
        data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        return data

    def get_post_req(self, url, data):
        try:
            req = requests.post(url, headers=self.headers, data=data)
            print("已连接上网易云音乐")
        except Exception as e:
            print(url)
            print(e)
        if req == "":
            print("什么都没有抓取到")
        else:
            # print(req.json())
            print(type(req.json()))
            print(req.json())
            final_file = songName + "_res.txt"
            file = open(final_file, 'a', encoding='utf-8')
            if 'hotComments' in req.json():
                print(req.json()['hotComments'])
                print(req.json()['hotComments'][0])
                print(type(req.json()['hotComments'][0]))
                for each in req.json()['hotComments']:
                    string = ""
                    string = each['content'] + "\t" + str(each['likedCount']) + "\n"
                    file.write(string)

            # we get all of the comments here, and write to txt
            with codecs.open(filename, 'a', encoding='utf-8') as f:       # here use the a mode to write the txt
                f.writelines(req.text)
        print("----------------")
        return req.json()

    # 偏移量
    def get_offset(self, offset):
        if offset == 0:
            text = {'rid': '', 'offset': '0', 'total': 'true', 'limit': '20', 'csrf_token': ''}
        else:
            text = {'rid': '', 'offset': '%s' % offset, 'total': 'false', 'limit': '20', 'csrf_token': ''}
        return text

    # 得到json格式的评论
    def get_json_data(self, url, offset):
        text = self.get_offset(offset)        # get the text of the request
        data = self.encrypted_request(text)   # calculate the data of the request
        json_text = self.get_post_req(url, data)   # send the request
        return json_text

    def get_song_comment(self):
        '''某首歌下全部评论 '''
        final_file = songName + "_res.txt"
        result_str = ""
        comment_info = []
        data = self.get_json_data(self.comment_url, offset=0)
        '''
        print(type(data))
        print(data)
        for com in data:
            file = open(final_file, 'a', encoding='utf-8')
            result_str = ""
            result_str = com['content'] + "\t" + str(com['likedCount']) + "\n"
            file.writelines(result_str)
        '''
        comment_count = data['total']
        #comment_count = 3
        if comment_count:
            comment_info.append(data)
        if comment_count > 20:
            for offset in range(20, int(comment_count), 20):
                if offset % 200 == 0:
                    time.sleep(random.randint(3, 8))
                print("开始爬取第{}页".format(offset/20))
                comment = self.get_json_data(self.comment_url, offset=offset)  # the type of comment is dict
                # print(comment['comments'])    # the type of comment['comments'] is list
                # print((comment['comments'][5]['content']))   # the type of comment['comments'][] is dict
                # print((comment['comments'][6]['content']))
                # print((comment['comments'][7]['content']))
                # print((comment['comments'][7]['likedCount']))
                for each in comment['comments']:
                    file = open(final_file, 'a', encoding='utf-8')
                    result_str = ""
                    result_str = each['content'] + "\t" + str(each['likedCount']) + "\n"
                    file.writelines(result_str)
                comment_info.append(comment)

        # file = open(final_file, 'w', encoding='utf-8')

        return comment_info

    def get_album_comment(self, comment_count):
        '''某专辑下全部评论 '''

        album_comment_info = []
        if comment_count:
            for offset in range(0, int(comment_count), 20):
                comment = self.get_json_data(self.comment_url, offset=offset)
                album_comment_info.append(comment)
        return album_comment_info

def save_to_file(list, filname):
    with codecs.open(filename, 'a', encoding='utf-8') as f:
        f.writelines(list)

    print("写入文件成功!")


start_time = time.time()
filename = songName + "_src.txt"
comment_url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + songID + '?csrf_token='
all_comment = []
craw_song_comments = CommentCrawl(comment_url)
print("开始")
all_comment = craw_song_comments.get_song_comment()
print("--------------")


end_time = time.time()  # 结束时间
print("程序耗时%f秒." % (end_time - start_time))
print("已完成")
