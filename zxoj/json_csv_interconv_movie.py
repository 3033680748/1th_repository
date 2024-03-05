import json
import csv
import sys
from copy import deepcopy

type_ = sys.argv[1]
input_file = sys.argv[2]

#合并
if type_ == "-b":
    output_file = input_file[:-3] + "json"
    lines = []
    dic = {}
    out_dic = []
    with open(input_file,"r") as f:
        datas = csv.reader(f)
        for line in datas:
            lines.append(line)

    for label in lines[0]:
        if "movie_author" in label:
            dic["movie_author"] = []
        else:
            dic[label] = None

    with open(output_file, "w") as f:
        for i in range(1, len(lines)):
            dic["movie_author"] = []
            for j in range(len(lines[i])): #
                if "movie_author" in lines[0][j]:
                    if lines[i][j] != "":
                        dic["movie_author"].append(lines[i][j])
                else:
                    if lines[0][j] == "movie_rating":
                        dic[lines[0][j]] = float(lines[i][j])
                    else:
                        dic[lines[0][j]] = lines[i][j]
            out_dic.append(deepcopy(dic))

        json.dump(out_dic,f,indent=4)

#分离
else:
    output_file = input_file[:-4] + "csv"
    with open(input_file,"r") as f:
        datas = json.load(f)

    label = list(datas[0].keys())
    num_author = 0
    for _ in range(len(datas)):
        num_author = max(num_author,len(datas[_]["movie_author"]))

    for idx, lab in enumerate(label):
        if lab == "movie_author":
            label.pop(idx)
            for i in range(1,num_author+1):
                label.insert(idx+i-1,"movie_author{}".format(i))
            break

    with open(output_file,"w",newline='') as f:
        writer = csv.DictWriter(f,label)
        writer.writeheader()
        for dic in datas:
            temp_author = list(dic["movie_author"])
            del dic["movie_author"]
            for i in range(1,len(temp_author)+1):
                idx = "movie_author{}".format(i)
                dic[idx] = temp_author[i-1]
            writer.writerow(dic)