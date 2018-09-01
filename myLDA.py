import pandas as pd
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer   # extract feature
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis
import pyLDAvis.sklearn
import os
import glob
import stop_words
import time

def chinese_word(mytext):
    return " ".join(jieba.cut(mytext))


def print_top_words(model, feature_names, n_topic_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


def loadData(filename):  # 从txt中读取每一行的数据，顺手将脏数据扔了，返回pandas的dataFrame类型的数据。
    data = []
    file = open(filename, 'r', encoding='utf-8')
    for line in file.readlines():
        line = line.strip().split('\t')   # split函数有点秀，如果没有'\t’则不会分割，也不报错。懒人专用
        if len(line[0]) > 2:
            data.append(line[0])
        else:
            print('dirty data')

    # df = pd.DataFrame({'dataFrame': data})
    return data


if __name__ == '__main__':
    start_time = time.time()
    os.chdir('data\\民谣\\')
    files = glob.glob('*_res.txt')
    data = []
    stop_word = stop_words.getStopWords()

    for fileName in files:
        data = data + loadData(fileName)

    df = pd.DataFrame({'dataFrame': data})
    df['content_cut'] = df['dataFrame'].apply(chinese_word)

    '''提取主要特征向量，上限为1000维'''
    n_features = 50
    tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                    max_features=n_features,
                                    stop_words=stop_word,
                                    max_df=0.5,
                                    min_df=10)
    tf = tf_vectorizer.fit_transform(df.content_cut)

    '''设定topic的数量，聚类为5类'''
    n_topics = 5
    lda = LatentDirichletAllocation(n_topics=n_topics,
                                    max_iter=50,
                                    learning_method='online',
                                    learning_offset=50.,
                                    random_state=0)

    '''开始聚类'''
    lda.fit(tf)

    '''设定topWord的个数，为20个。   并初始化各个feature的name'''
    n_top_words = 20
    tf_feature_names = tf_vectorizer.get_feature_names()
    print_top_words(lda, tf_feature_names, n_top_words)
    pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
    print("END, use time %f" % (time.time() - start_time))
