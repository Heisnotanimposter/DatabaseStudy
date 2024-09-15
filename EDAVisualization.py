%matplotlib inline

%config InlineBackend.figure_format = 'retina'

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import pandas as pd

import numpy as np

plt.savefig ('lemon.png')

year = [1,2,3,4,] ; pop = [4,3,2,1,]
plt.plot(year,pop)
plt.title('Matplotlib1'
plt.show()

year = [1,2,3,4] ; pop = [4,3,2,1]
fig,ax = plt.subplots (nrows = 1, ncols=1)
ax.set_title(Matplotlib2)
ax.plot(year, pop)

dic = dict (year = [1,2,3,4], pop = [4,3,2,1])
df = pd.DataFrame(dic)

df.plt(x = 'year', y = 'pop' ,kind = 'line')
plt.title('Pandas')

df

plt.scatter(year.pop) ; plt.show()

drinks.plor (kind='scatter', x='beer', y = 'wine', alpha = 0.4)

drinks.plot (kind='scatter', x='beer', y= 'wine', c= 'spirit', colormp = 'Blues')

pd.scatter_matrix(drinks[['beer','sprite','wine']], figsize = (10,8))

values = [0,1,2,3,4,5,6]
plt.hist(values, bins = 6, color = 'red') ; plt.show()

df.hist(column = 'col1', by = 'col2', sahrex = True, sharey = True, layout=(2,3))

values = [0,1,2,3,4,5,6]
plt. boxplot(values) ; plt.show()
plt.boxplot(values, vert = 0) ; plt.show()

objects = ['a','b','c','d','e']
performance = [5,4,3,2,1]
plt.bar(objects, performance) ; plt.show()

drinks.groupby('continent').mean().drop('liters', axis = 1).plot(kind = 'bar')

drinks.groupby('continents').mean().drop('liters',axis = 1). plot(kind='bar')

plt.pie(performance, labels = objects) ; plt.show()

year = [5,4,3,2,1] ; pop = [1,2,3,4,5]
plt.figure(figsize=(10,3))
plt.plot(year,pop)

plt.xlabel('year')
plt.ylabel('population')

plt.title('World Population Projections') ; plt.show(0)

plt.plot(year, pop)
plt.yticks([0,2,4,6,8], ['a','b','c','d','e']) ; plt.show()

year = [1,2,3,4,5]
pop1 = [3,4,5,6,7]
pop2 = [4,5,6,7,8]

plt.plot(year, pop1, 'red')
plt.plot (year, pop2, ' Blue') ; plt.show()


import pandas as pd

aq = pd.read_csv('csvpath') ; 
ti = pd.read_csv('samplepath')

aq. plot(kind = "scatter", x= "temp", y ="Ozone")

ti.plot(kind = 'hist', y = "Age", bins = 16, grid = 1)

ti__grouped = ti.groupby(["Pclass","se"])["Age"].ean()
ti_grouped.plot(kind = "bar" , color = ['red','orange','yellow','green','blue','black']) ; 

ri.plot(kind = "box", y = "Age")

ti.boxplot("Age", by = ["Survuved","Pclass", grid = False])

import pandas as pd
import matplotlib.pyplot asplt
imoprt seaborn as sns

sns. kdeplot(aq)