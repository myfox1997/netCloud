import numpy
import os
import glob


def loadData(filename, sentiment):
    count = [0, 0, 0]
    data = []
    file = open(filename, 'r', encoding='utf-8')
    for line in file.readlines():
        line = line.strip().split('\t')   # split函数有点秀，如果没有'\t’则不会分割，也不报错。懒人专用
        if len(line[0]) > 0:
            # data.append(line[0])
            try:
                sentiment[line[2]] += 1
            except KeyError as ke:
                sentiment[line[1]] += 1
        else:
            print('dirty data')

    # df = pd.DataFrame({'dataFrame': data})
    return sentiment


if __name__ == '__main__':
    os.chdir('data\\摇滚感情\\')
    files = glob.glob('*.txt')

    sentiment = {'positive': 0, 'mid': 0, 'negative': 0}
    for file in files:
        loadData(file, sentiment)
    print(sentiment)

