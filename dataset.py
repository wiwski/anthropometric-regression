import re
import json

data = []
f = open('ansur_men.txt', 'r')
for line in f:
    data.append(re.split(r'\t+', line[:-1]))

f.closed
dataCurated = []
for d in data:
    dataCurated.append([d[112], d[99], d[123], d[33], d[81]])

with open('dataset.txt', 'w') as fw:
    json.dump(dataCurated, fw)
fw.closed

#print(data[0][112]) //WAIST
#print(data[0][99]) //STATURE
#print(data[0][123]) //WEIGHT
#print(data[0][33]) //CHEST
#print(data[0][81]) //NECK
