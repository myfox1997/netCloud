# !/usr/bin/env python
# coding: utf-8
'''

'''

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class MyCrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def myencrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        text = text.encode('utf-8')
        count = len(text)
        add = length - (count % length)
        text = text + (b'\0' * add)

        # print len(text)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext).decode("ASCII")

    def mydecrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip(b'\0').decode('utf-8')

if __name__ == '__main__':
    mycrypt = MyCrypt('abcdefghjklmnopq')
    e = mycrypt.myencrypt('hello,world!')
    d = mycrypt.mydecrypt(e)
    print (e)
    print (d)