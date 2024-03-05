import sys
import json


name = sys.argv[1]

with open(name,"r",encoding="utf-8") as f:
    tuple_ = tuple(json.load(f))

dic = {}

for num in tuple_:
    try:
        dic[num] += 1
    except KeyError:
        dic[num] = 0
        dic[num] += 1

dic_ = sorted(dic.items(),key=lambda x:x[1],reverse=True)

max_ = -1
out = []
for i in range(len(dic_)):
    if max_ <= dic_[i][1]:
       out.append(dic_[i][0])
       max_ = dic_[i][1]
    else:
        break

with open("output.txt", 'w') as f:
    for i in range(len(out)):
        if i != len(out)-1:
            f.write("{:d}".format(out[i]))
            f.write(',')
        else:
            f.write("{:d}".format(out[i]))


