import jieba
from snownlp import SnowNLP
from snownlp import tag
from snownlp import sentiment
import numpy
import time


text_JB = '我今天感觉有些难受'
text_S = u'我今天感觉有些难受'
text_S2 = u'我现在十分生气'

file = open('铅球.txt', 'rt', encoding="utf-8")
'''
print("Full Mode: ", "/".join(seg_list))

snow_ans = SnowNLP(text_S)
print("Snow_ans", "/".join(snow_ans.words))
print(snow_ans.sentiments)

snow_ans2 = SnowNLP(text_S2)
print("Snow_ans", "/".join(snow_ans2.words))
print(snow_ans2.sentiments)
'''
start_time = time.time()
data = []
for line in file.readlines():
    curline = line.strip().split(' ')
    curline = list(curline)
    data.append(curline)

dataMat = numpy.array(data)

print(dataMat)

ansMat = []
ans = []
for row in dataMat:
    ans = []
    snow_ans = SnowNLP(str(row[5]))
    if snow_ans.sentiments > 0.6:
        print(str(row[5]), "optimism", str(snow_ans.sentiments))
        ans.append(str(row[5]))
        ans.append('   optimism    ')
        ans.append(str(snow_ans.sentiments))
    else:
        print(str(row[5]), "negative", str(snow_ans.sentiments))
        # ans.append(str(row[5]))
        ans.append(str(row[5]))
        ans.append('    negative    ')
        ans.append(str(snow_ans.sentiments))
    ansMat.append(ans)


print(ansMat)
file_wirte = open('ans.txt', 'w')
for lines in ansMat:
    file_wirte.write(lines[0] + lines[1] + lines[2] + '\n')

end_time = time.time()
print("END")
print('用时%f秒' % (end_time - start_time))


