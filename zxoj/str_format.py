import sys

def reforce(s:str)->str:
    out = ""
    operate_time = 0
    for item in s:
        if '0' <= item <= '9':
            out += item
            operate_time += 1
            if operate_time % 3 == 0:
                out += "-"
    if s[-1] == '\n':
        out = out[:-1]+"\n"
    else:
        out = out[:-1]
    return out


input_file = sys.argv[1]
output_file = sys.argv[2]

str_ = ""

with open(input_file,"r") as f:
    while 1:
        s = f.readline()
        if s == '':
            break
        else:
            str_ += reforce(s)

with open(output_file,"w") as f:
    f.write(str_)