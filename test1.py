# %%
import csv

i = 0
with open('data/AAPLUSUSD_H4.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0].split('\t'))
        i += 1
        if i > 7:
            break

print('######################################################')

# %%
i = 0
with open('data/AAPLUSUSD_H4.csv', 'r', encoding='utf-8') as f:
    for row in f:
        print(row.strip().split('\t'))
        i += 1
        if i > 7:
            break

print('######################################################')
