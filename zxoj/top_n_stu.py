import sys
import json

file_path = sys.argv[1]

n = int(sys.argv[2])

with open(file_path,"r") as f:
    data = f.read()
    dic = dict(json.loads(data))

dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)

with open("output.csv","w") as f:
    for _ in range(n):
        f.write("{}".format(dic[_][0]))
        if _ < n-1:
            f.write(",")

