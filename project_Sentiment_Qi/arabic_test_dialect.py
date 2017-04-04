import xlrd
book = xlrd.open_workbook("bbn_shared.xls")
sh_test = book.sheet_by_index(0)

from repustate import Client
client = Client(api_key='6d4558d42cf6a2e509c8b4c0184229c443f2d44d', version='v3')
count = 0
num = 400
for i in range(0,num):
    f = client.sentiment(sh_test.cell(i,0),"ar")
    #print(f['score'])
    #print(sh_test.cell(i,1))
    g = sh_test.cell(i,1).value
    if f['score'] > 0:
        if [g] == ['Positive']:
            count = count + 1
        else:
            count = count
    elif f['score'] < 0:
        if g is "Negative":
            count = count+1
        else:
            count = count
    elif f['score'] == 0:
        if g is "Neutral":
            count = count+1
        else:
            count = count
    else:
        count = count
    #print(count)
print(count/num)


