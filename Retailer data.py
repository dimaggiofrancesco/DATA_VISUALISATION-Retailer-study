import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# -------------------- LOAD cvs FILE --------------------
df = pd.read_csv('products_sample.csv')

# -------------------- COLUMNS FORMAT --------------------
df['price']= df.price.astype(int)
df['max_discount']= df.max_discount.astype(float)
df['date']= df['date'].astype ('datetime64[D]')
df['date_first_sellout']=df['date_first_sellout'].astype ('datetime64[D]')
df['date_first_sellthrough']=df['date_first_sellthrough'].astype ('datetime64[D]')

# -------------------- GRAPH 1: Discount per category --------------------
graph = df.groupby(['category', 'currency'])['max_discount'].mean().unstack()
plot = graph.plot.bar(title = "GRAPH 1: Discount per category", fontsize = 8)
g1 = graph

plot.set_xlabel("category")
plot.set_ylabel("mean of the maximum discounts")
plot.set_yticklabels(['{:.0%}'.format(x) for x in plot.get_yticks()])
plt.legend(bbox_to_anchor=(0.7,0.85), loc="lower center",fontsize=10,ncol=1, borderaxespad=0.)
plt.show()

# -------------------- GRAPH 2a: Absolute percentage of options that did not sell-out --------------------
table = df.groupby(['category', 'currency'])
graph = 1 - (table.count()['date_first_sellout'] / table.size()).unstack()
g2 = graph

plot = graph.plot.bar(legend = False, fontsize = 7, title = "GRAPH 2a: Absolute percentage of not sell-out options")
plot.set_ylabel("Absolute percentage of not sell-out options")
plot.set_yticklabels(['{:.0%}'.format(x) for x in plot.get_yticks()])
plt.legend(bbox_to_anchor=(0.9,0.85), loc="lower center",fontsize=10,ncol=1, borderaxespad=0.)
plt.show()

# -------------------- GRAPH 2b: Relative % of stock per category that did not sell-out --------------------
data = {'percentage' : []}
indices = []
for category in df.category.unique():
    partial = df[df['category'] == category]
    data['percentage'].append(1 - partial.count()['date_first_sellout'] / len(partial))
    indices.append(category)
graph = pd.DataFrame(data, index = indices)

plot = graph.plot.pie(subplots = True, autopct = '%.1f%%', fontsize = 7, legend = False,
                      title = 'GRAPH 2b: Relative percentage of not sell-out options')
plt.ylabel('')
plt.show()

# -------------------- GRAPH 3: Correlation between discount percentage and percentage of options that did not-sell out
s = plt.scatter(g1['GBP']*100,g2['GBP']*100)
z1 = np.polyfit(g1['GBP']*100,g2['GBP']*100, 1)
p1 = np.poly1d(z1)
t = plt.scatter(g1['USD']*100,g2['USD']*100)
z2 = np.polyfit(g1['USD']*100,g2['USD']*100, 1)
p2 = np.poly1d(z2)

plt.title ('GRAPH 3: Correlation between discount percentage and \n percentage of options that did not-sell out')
plt.xlabel("Applied discount (percentage)")
plt.ylabel("Options that did not sell-out (percentage)")
plt.plot(g1['GBP']*100,p1(g1['GBP']*100),"r--", color = 'blue', label = 'GBP')
plt.plot(g1['USD']*100,p2(g1['USD']*100),"r--", color = 'orange', label = 'USD')
plt.show()

# -------------------- GRAPH 4a: Footwear discount per month --------------------
graph = df[df['category'] == 'footwear'].groupby([df['date'].dt.month, 'currency'])['max_discount'].mean().unstack()

plot = graph.plot(title = "GRAPH 4a: Footwear discount per month",style='.-')
plot.set_xlabel("month")
plot.set_ylabel("mean of the maximum discounts")
plot.set_yticklabels(['{:.0%}'.format(x) for x in plot.get_yticks()])
plot.set_xticklabels(['','Feb', 'Apr', 'Jun', 'Aug', 'Oct', 'Dec'])
plt.show()

# -------------------- GRAPH 4b: Footwear price per month --------------------
graph = df[df['category'] == 'footwear'].groupby([df['date'].dt.month, 'currency'])['price'].mean().unstack()

plot = graph.plot(title = "GRAPH 4b: Footwear price per month",style='.-')
plot.set_xlabel("month")
plot.set_ylabel("mean of the maximum price")
plot.set_xticklabels(['','Feb', 'Apr', 'Jun', 'Aug', 'Oct', 'Dec'])
plt.ylim(ymin=250, ymax=550)
plt.show()

# -------------------- GRAPH 5: Distrubution of the days spent from the goods arrival to the sell_out --------------------
df2 = df[df['currency']==('GBP')]
dresses_so = df2[df2['category'] == 'footwear']
data_so = (dresses_so['date_first_sellout'] - dresses_so['date']).apply(lambda v: v.days)
graph5_so = data_so[data_so.notna()]
plt.hist(graph5_so, alpha=0.5, bins=35, color='blue', edgecolor='black', label='GBP')

df3 = df[df['currency']==('USD')]
dresses_so = df3[df3['category'] == 'footwear']
data_so = (dresses_so['date_first_sellout'] - dresses_so['date']).apply(lambda v: v.days)
graph5_so = data_so[data_so.notna()]

plt.hist(graph5_so, alpha=0.5, bins=35, color='orange', edgecolor='black', label='USD')
plt.title('GRAPH 5: Distribution of the days spent \n from the footwear option arrival to the sell_out')
plt.xlabel('days')
plt.legend(loc='upper right')
plt.xlim(xmin=0, xmax=450)
plt.show()
