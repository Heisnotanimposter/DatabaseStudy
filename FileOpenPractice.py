import os 
os.getced()

data = open('path', 'r', encoding = 'cp949')
line = data.read()

line

line = line.split('\n')

line

row = []
#row is horizontal numbering, col is vertical numbering.
for i in line:
	row.append(i.split(','))
print(row)

import pandas as pd
col_nm = ['num','name','age','tall']
df = pd.Dataframe(row, columns = col_nm)

col_num = ['num', 'age' , 'tall']
df = pd.DataFrame(row, columns = col_nm)

col_num = ['num', 'age' , 'tall']
for i in colnum:
	df[i] = df[i]astype('int')

df

df.dtypes

data2 = open('path', 'r' , 'cp949')
line2 = data2.read()

line2 = line2. split('\n')

line2

col_nm = line2[0].split(',')
col_nm

line2 = line2[1:]

row = []
for i in line2:
	row.append(i.split(','))
row

df = pd.DataFrame(row, columns = col_nm)

col_num = ['num','age','tall']
for i in col_num:
	df[i] = df[i].astype('int')

df

df.dtypes

data3 = open('data3path','r',encoding='cp949')

line3 = data3.read()
line3

line3 = line3. split('\n')
line3

row = []
for i in line3 : 
	row.append(i.split('\t'))
print(row)

col_nm = row[0]
print(col_nm)
row = row [1:]
print(row)

df = pd.DataFrame(row, columns = col_nm)

col_num = ['num','age','tall']
for i in col_num:
	df[i] = df[i].astype('int')
df

data4 = open('data4path','r', encoding = 'cp949')
line4 = data4. read()
line4

line4 = line4.split('?')
line4

row = []
for i in line4:
	row.append(i.split(','))
row

col_nm = ['num','name','age','tall']
df = pd.DataFrame(row,columns = col_nm)

col_num = ['num','age','tall']
for i in col_num:
	df[i] = df[i],astype('int')

df

data5 = open('data5path','r',encoding='cp949')
line5 = data5.read()
line5

line5 = line5.split(',')
line5

row = []
for i in range(0, len(line5), 4):
	row.append(line5[i : i+4])
row

df = pd.DataFrame(row, columns = ['num','name','age','tall'])

col_num = ['num', 'age','tall']
for i in columnnumber:
	dataframe[i] = dataframe[i].astype('int')

dataframe

data6 = open('data6path','r',encoding = 'cp949')
line6 = data6.read()
line6

line6 = line6.split(',')
line6

row = []

for i in range(0, len(line6), 3:
	row.append (line6[i:i+3])
row

row = []
for i in range(0,len(line6), 5) : 
	row.append(line6[i:i+5])
row

data7 = open('data7path','rb')
#rb is standing for read by byte
line7 = data7.read()
line7[:100]

word = ''.encode('utf-8')
word

word.decode('utf-8')

data9 = open('data9path')
line9 = data9.read()
line9[:200]

line9 = line9.split('\n')
line9[:5]

row = []
for i in line9:
	row.append(i.split(','))
row

col_nm = row[0]
row = row[1:]
df =  pd.DataFrame(row, columns = col_nm)
df.head()

