import json,codecs,csv

file = open('annotations.txt', 'r', encoding='UTF-8')
js = file.read();
dic = json.loads(js);
list_aOq = dic["annotationsOfQueries"]

headers = ['query','keywords']

fcsv = open("annotations.csv", 'a',newline='')
f_csv = csv.writer(fcsv)
f_csv.writerow(headers)

for lv in list_aOq:
    keywords = []
    for l in lv['annotations']:
        keywords.append(l['value'])


    f_csv.writerow([lv['query'],';'.join(keywords)])  #keyword不能空格输入，因为会有词组本身有空格
