#!/usr/bin/env python

import xlrd

xls = xlrd.open_workbook(r'bbn_shared-2.xls')
print(xls.sheet_names())

sheet = xls.sheet_by_index(0)
print(sheet.name, sheet.nrows, sheet.ncols)

nrows = sheet.nrows
ncols = sheet.ncols
data = []
label = []
pos = 0
neg = 0
neu = 0
for line in range(1, nrows):
    senti = sheet.cell_value(line, 1)
    text = sheet.cell_value(line, 0)
    if senti != 'Both':
        data.append(text)
        label.append(senti)
    if senti == 'Positive':
        pos = pos + 1
    if senti == 'Negative':
        neg = neg + 1
    if senti == 'Neutral':
        neu = neu + 1
# print('len of data and label:', len(data), len(label))
# print(pos, neg, neu)
# nrows_test = round(nrows * 2 / 3)
# print(nrows_test)
# print(len(data[nrows_test:nrows - 1]))


def get_data():
    return data[0:399], label[0:399]
