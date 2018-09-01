from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import os
import glob
import time

start_time = time.time()
os.chdir('data\\摇滚\\')
files = glob.glob('*_res.txt')
print(files)
# comment_text = open('123我爱你_res.txt', 'r', encoding='utf-8').read()
comment_all = ''
for each in files:
    comment_text = open(each, 'r', encoding='utf-8').read()
    comment_all = comment_all + comment_text

cut_text = " ".join(jieba.cut(comment_all))
# background_img = plt.imread('img.png')
# print("load the img successfully ")
could = WordCloud(
    font_path='迷你简行楷.TTF',
    background_color='white',
    max_words=2000,
    max_font_size=40,
    width=1280,
    height=1080
)
word_cloud = could.generate(cut_text)
word_cloud.to_file('test.png')

plt.imshow(word_cloud)
plt.axis('off')
plt.show()
end_time = time.time()
print("END, use time %f" % (end_time - start_time))
'''
wc = WordCloud(background_color='white', width=1000, height=860, margin=2).generate(f)
plt.imshow(wc)
plt.axis('off')
plt.show()
'''


