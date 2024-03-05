import json
import re
import sys

def output(obj):
    print(json.dumps(obj))

file_path = sys.argv[1]

with open(file_path,"r") as f:
    datas = f.read()

datas = datas.lower()
datas = re.split("\W+", datas)
# print(datas)


dic = {}
for word in datas:
    if word == '':
        continue
    else:
        try:
            dic[word] += 1
        except KeyError:
            dic[word] = 1

output(dic)
