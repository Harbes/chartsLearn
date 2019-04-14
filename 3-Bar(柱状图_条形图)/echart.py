import pandas as pd

tab = pd.read_excel('data/course_orders.xlsx')
print(tab.head(10))

count = tab.groupby("商品名称")["订单编号"].count().sort_values(ascending=False)
x = count.index.tolist()
y = count.values.tolist()

from pyecharts import Bar

bar = Bar("松鼠学堂课程销量统计","付费课程学员数量统计")
bar.add("学员人数",x,y)
bar.render('aaa.html')