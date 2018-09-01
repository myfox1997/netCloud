import os
import glob


def loadData(filename, sentimentHot, sentimentNormal):
    count = [0, 0, 0]
    data = []
    file = open(filename, 'r', encoding='utf-8')
    for line in file.readlines():
        line = line.strip().split('\t')   # split函数有点秀，如果没有'\t’则不会分割，也不报错。懒人专用
        # print(line)
        if len(line[0]) > 0:
            try:
                if int(line[1]) > 50:
                    sentimentHot[line[2]] += int(line[1])  # sentiment of the comment ,  like of the comment
                else:
                    sentimentNormal[line[2]] += int(line[1])
            except KeyError as ke:
                if int(line[0]) > 50:
                    sentimentHot[line[1]] += int(line[0])
                else:
                    sentimentNormal[line[1]] += int(line[0])
            except ValueError as ve:
                print("error")

        else:
            print('dirty data')

    # df = pd.DataFrame({'dataFrame': data})
    return sentimentHot, sentimentNormal


if __name__ == '__main__':
    os.chdir('data\\轻音乐感情\\')
    files = glob.glob('*.txt')
    sentimentHot = {'positive': 0, 'mid': 0, 'negative': 0}
    sentimentNormal = {'positive': 0, 'mid': 0, 'negative': 0}
    for file in files:
        loadData(file, sentimentHot, sentimentNormal)
    print("Hot\n", sentimentHot)
    print("Normal\n", sentimentNormal)
