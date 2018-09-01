from sklearn.feature_extraction.text import CountVectorizer
import jieba
import pandas as pd


def loadData(filename):  # 从txt中读取每一行的数据，顺手将脏数据扔了，返回pandas的dataFrame类型的数据。
    data = []
    file = open(filename, 'r', encoding='utf-8')
    for line in file.readlines():
        line = line.strip().split('\t')   # split函数有点秀，如果没有'\t’则不会分割，也不报错。懒人专用
        if len(line[0]) > 2:
            data.append(line[0])
        else:
            print('dirty data')

    df = pd.DataFrame({'dataFrame': data})
    return df


def chinese_word(mytext):
    return " ".join(jieba.cut(mytext))


if __name__ == '__main__':
    fileName = '123我爱你_res.txt'
    df = loadData(fileName)

    df['content_cut'] = df['dataFrame'].apply(chinese_word)  # 利用jieba对于每一行数据分词并返回

    n_features = 50  # 设置最大feature的数量，50是我随便写的。
    # print(df['content_cut'])
    # 初始化CountVectorizer的参数
    tf_vectorizer = CountVectorizer(max_features=n_features,
                                    strip_accents='unicode',
                                    stop_words='english')
    tf = tf_vectorizer.fit_transform(df.content_cut)

    print(tf_vectorizer.get_feature_names())  # 这里是features的name， type == list
    print(tf.toarray())  # 这里是每一行数据的vector，type == list
    # ary = tf.toarray()

    ENGLISH_STOP_WORDS = frozenset([
        "a", "about", "above", "across", "after", "afterwards", "again", "against",
        "all", "almost", "alone", "along", "already", "also", "although", "always",
        "am", "among", "amongst", "amoungst", "amount", "an", "and", "another",
        "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are",
        "around", "as", "at", "back", "be", "became", "because", "become",
        "becomes", "becoming", "been", "before", "beforehand", "behind", "being",
        "below", "beside", "besides", "between", "beyond", "bill", "both",
        "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con",
        "could", "couldnt", "cry", "de", "describe", "detail", "do", "done",
        "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else",
        "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
        "everything", "everywhere", "except", "few", "fifteen", "fifty", "fill",
        "find", "fire", "first", "five", "for", "former", "formerly", "forty",
        "found", "four", "from", "front", "full", "further", "get", "give", "go",
        "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
        "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his",
        "how", "however", "hundred", "i", "ie", "if", "in", "inc", "indeed",
        "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter",
        "latterly", "least", "less", "ltd", "made", "many", "may", "me",
        "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly",
        "move", "much", "must", "my", "myself", "name", "namely", "neither",
        "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone",
        "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on",
        "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our",
        "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
        "please", "put", "rather", "re", "same", "see", "seem", "seemed",
        "seeming", "seems", "serious", "several", "she", "should", "show", "side",
        "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
        "something", "sometime", "sometimes", "somewhere", "still", "such",
        "system", "take", "ten", "than", "that", "the", "their", "them",
        "themselves", "then", "thence", "there", "thereafter", "thereby",
        "therefore", "therein", "thereupon", "these", "they", "thick", "thin",
        "third", "this", "those", "though", "three", "through", "throughout",
        "thru", "thus", "to", "together", "too", "top", "toward", "towards",
        "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us",
        "very", "via", "was", "we", "well", "were", "what", "whatever", "when",
        "whence", "whenever", "where", "whereafter", "whereas", "whereby",
        "wherein", "whereupon", "wherever", "whether", "which", "while", "whither",
        "who", "whoever", "whole", "whom", "whose", "why", "will", "with",
        "within", "without", "would", "yet", "you", "your", "yours", "yourself",
        "yourselves"])



