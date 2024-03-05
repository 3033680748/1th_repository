import sys
import json

data_name = sys.argv[1]

with open(data_name,"r") as f:
    string = f.read()

string = string.lower()
li = []

for char in string:
    if ord('a') <= ord(char) <= ord('z'):
        li.append(char)

check = 0
result = "true"
for i in range(len(li)//2):
    if li[i] == li[len(li)-1-i]:
        continue
    else:
        check = -1
        break

if check == -1:
    result = "false"

input_ = ""

for elem in li:
    input_ += elem

with open("output.json","w",encoding="utf-8") as f:
    json.dump({'palindrome':result,'result':input_},f)

