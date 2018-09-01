import pandas as pd
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer   # extract feature
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis
import pyLDAvis.sklearn

df = pd.read_csv('datascience.csv', encoding='gb18030')


def chinese_word(mytext):
    return " ".join(jieba.cut(mytext))


def print_top_words(model, feature_names, n_topic_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


if __name__ == '__main__':
    df['content_cutted'] = df.content.apply(chinese_word)
    # print(df.content_cutted.head())

    '''提取主要特征向量，上限为1000维'''
    n_features = 1000
    tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                    max_features=n_features,
                                    stop_words='english',
                                    max_df=0.5,
                                    min_df=10)
    tf = tf_vectorizer.fit_transform(df.content_cutted)

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

