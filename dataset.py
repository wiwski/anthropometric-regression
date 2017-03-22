import re
import json

data = []
f = open('ansur_men.txt', 'r')
for line in f:
    data.append(re.split(r'\t+', line[:-1]))

f.closed
dataCurated = []
dataCurated.append([data[0][112], data[0][99], data[0][123], data[0][33], data[0][81]])
for d in data[1:]:
    dataCurated.append([int(d[112]), int(d[99]), int(d[123]), int(d[33]), int(d[81])])

with open('dataset.txt', 'w') as fw:
    json.dump(dataCurated, fw)
fw.closed

#print(data[0][112]) //WAIST
#print(data[0][99]) //STATURE
#print(data[0][123]) //WEIGHT
#print(data[0][33]) //CHEST
#print(data[0][81]) //NECK
