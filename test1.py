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




