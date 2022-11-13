# %%
import csv

i = 0
with open('data/AAPLUSUSD_H4.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        i += 1
        if i > 7:
            break

# %%
import csv

i = 0
with open('data/AAPLUSUSD_H4.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0].split('\t'))
        i += 1
        if i > 3:
            break

# %%
i = 0
rows = []
with open('data/AAPLUSUSD_H4.csv', 'r', encoding='utf-8') as f:
    for row in f:
        print(row.strip().split('\t'))
        rows.append(row.strip().split('\t'))
        i += 1
        if i > 3:
            break

# %%
i = 0
rows = []
with open('data/AAPLUSUSD_H4.csv', 'r', encoding='utf-8') as f:
    for row in f:
        #print(row.strip().split('\t'))
        rows.append(row.strip().split('\t'))
        i += 1
        if i > 3:
            break

rows_dict = [dict(zip(rows[0], row)) for row in rows[1:]]

print(rows_dict)

# %%
import json
with open('data/test.json', 'w', encoding='utf-8') as f:
    json.dump(rows_dict, f, ensure_ascii=False, indent=4)

# %%
import pandas as pd
df = pd.DataFrame(data=rows[1:], columns=rows[0])
json_rows = df.to_json('data/test_pandas.json', orient='records')



# %%
#read the json data back
import json

with open('data/test.json', 'r') as f:
    reader = json.load(f)
    #print(reader)

openvalues = {}

#find the time of the highest Open value
for item in reader:
    #print(item) #{'Time': '2017-02-02 04:00:00', 'Open': '129.984', 'High': '130.48', 'Low': '128.78', 'Close': '128.785', 'Volume': '60'}
    openvalues[float(item['Open'])] = item['Time']

print('Open values available with timestamps')
print(openvalues)

openkeys = list(openvalues.keys())

print('Open values available as list of keys')
print(openkeys)

print('Sort the keys desc order')
openkeys.sort(reverse=True)

print(openkeys)

print('highest open value:')
print(openkeys[0])
print('timestamp of highest open value:')
print(openvalues[openkeys[0]])


with open('data/test.json', 'r') as r:
    reader = json.load(r)
    for row in reader:
        print(row)
