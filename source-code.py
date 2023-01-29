########## 柱状图
import matplotlib.pyplot as plt
# 设置中文字体和负号
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False 

# 设置韩文字体和负号
sns.set(font="AppleGothic",
            rc={"axes.unicode_minus":False}, style="darkgrid")

data = pd.read_excel(path)
data.sort_values(by='分数', inplace=True, ascending=False)
plt.bar(data.name, data.分数, label="成绩")
plt.xlabel("姓名")
plt.ylabel("分数")
plt.xticks(data.name, rotation=45)     # x轴旋转45度
plt.ylim([-30, 120])
plt.tight_layout() # 紧凑型布局
plt.title("三年二班学生成绩",fontsize=16, fontweight='bold')
plt.legend() # 显示图例 
plt.savefig(path)
plt.show()
#############


############# 条形图
data.sort_values(by='分数', inplace=True, ascending=False)
plt.bar(x=0, bottom=data.name, height=0.5, width=data.分数, color='red',
        orientation='horizontal', alpha=0.5) # alpha 透明度
plt.xlabel("分数", fontsize=20)
plt.ylabel("姓名", fontsize=20)
plt.title("")
plt.show()
#############


############# 分组柱状图
data.sort_values(by='第二年', inplace=True, ascending=False）
宽度=0.3
plt.bar(x=data.name, height=data.第一年, color='red', width=宽度, label='第一年')
plt.bar(x=np.arrange(len(data.姓名))+宽度, height=data.第二年, color='blue'
        width=宽度, label='第二年')
plt.legend()
plt.xticks(data.name)
轴=plt.gca()
轴.set_xticklabels(data.name, rotation=45, ha='center')   # 设置旋转参数

图形 = plt.gcf()
图形.subplots_adjust(left=0.1, bottom=0.3)  # 设置图离左边0.1的距离， 离下面0.3的距离
plt.show()
#############


############# 添加数据标签
for x, y1 in enumerate(data, 第一年):
    plt.text(x,y1+1, str(y1), fontsize=20, rotation=0, ha='center',va='bottom',color='blue')

for x, y2 in enumerate(data, 第二年):
    plt.text(x+宽度,y2+1, str(y2), fontsize=20, rotation=0, ha='center',va='bottom')
plt.show()
#############


############# 叠加柱状图
data = pd.read_excel(path)
plt.bar(np.arange(9), data.语文, color='red', label='语文')
plt.bar(np.arange(9), data.数学, bottom=data.语文, color='green', label='数学')
plt.bar(np.arange(9), data.英语, bottom=data.语文+data.数学, color='blue', label='英语')
# 设置x轴标签
plt.xticks(np.arange(9), data.name)
# 图例
plt.legend(loc='upper center', ncol=3） # 横着排，一行三列
# 改y轴刻度
plt.ylim([10,350])
# 加网格线
#plt.grid()
for x1, y1 in enumerate(数据.语文):
    plt.text(x1, y1-10, str(y1), color='white', fontsize=20, ha='center') 
for x2, y2 in enumerate(数据.语文 + 数据.数学):
    plt.text(x2, y2-10, str(y2), color='white', fontsize=20, ha='center') 
for x3, y3 in enumerate(数据.语文 + 数据.数学 + 数据.英语):
    plt.text(x3, y3-10, str(y3), color='white', fontsize=20, ha='center') 
plt.show()
#############


############# 叠加条形图
plt.bar(x=0, bottom=数据.姓名, height=0.5, width=数据.语文, orientation='horizontal', color='red')

plt.bar(x=数据.语文, bottom=数据.姓名, height=0.5, width=数据.数学, orientation='horizontal', color='green')

plt.bar(x=数据.语文+数据.数学, bottom=数据.姓名, height=0.5, width=数据.英语, orientation='horizontal', color='blue')

for x1, y1 in enumerate(数据.语文):
    plt.text(y1-20, x1, str(y1), ha='center', va='center',fontsize=20, color='white')

for x2, y2 in enumerate(数据.语文+数据.数学):
    plt.text(y2-20, x2, str(y2), ha='center', va='center',fontsize=20, color='white')

for x3, y3 in enumerate(数据.语文+数据.数学+数据.英语):
    plt.text(y3-20, x3, str(y3), ha='center', va='center',fontsize=20, color='white')
plt.show()
#############


############# 饼图
plt.pie(x=data.第一次, labels=tuple(数据.姓名), explode=(0, 0.2, 0), colors=['r', 'g', 'b'], autopct='%.2f%%', startangle=90, counterclock=False, labeldistance=0.8, pctdistance=0.3, textprops={'fontsize':20, 'color':'w'}) 
plt.pie(x=data.第二次, radius=0.5)
# 默认为逆时针，设置顺时针 counterclock=False
# 可设置起始位置方向 (startangle=90)
# explode=(0, 0.2, 0) 用于突出显示某块数据
# explode=(0, -0.2, 0) 可缩进某块数据
# 显示百分比 autopct='%.2f%%'  # %% 显示为百分号
# 设置标签与图的距离 labeldistance=0.8  默认为1.1
# 设置百分比标签与图的距离 pctdistance=0.3 默认为0.6
# 字大小与颜色设置 textprops={'fontsize':20, 'color':'w'}
plt.axis('equal'). # 将饼图变成正圆
plt.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1,1, 1.05), borderaxespad=0.3, ncol=3)
plt.savefig(r"c:\饼图.jpg", dpi=200, bbox_inches='tight')
plt.show()
#############


############# 3D饼图
plt.pie(x=数据.第一次, labels=tuple(data.name), explode(0,0,0.2), shadow=True)
plt.show()
#############


############# 折线图
plt.plot(数据.时间, 数据.蔬菜, color='r', marker='*', ms=10) # ms=10 数据点大小
plt.plot(数据.时间, 数据.水果, color='g', marker='o', ms=10)
plt.plot(数据.时间, 数据.食品, color='b', marker='^', ms=10)
plt.plot(数据.时间, 数据.用品, color='y', marker='v', ms=10)
for z in [数据.蔬菜, 数据.水果, 数据.食品, 数据.用品]:
    for x, y in zip(数据.时间, z):
        plt.text(x,y+0.7,str(y),ha='center', va='center', fontsize=20, rotation=0)
plt.show()
#############


############# 平均线
plt.bar(数据.班级, 数据.销售量, color='r', label='销售量', alpha=0.6) # alpha 透明度
plt.legend()
# 计算平均线
平均线 = np.mean(数据.销售量)
plt.axhline(y=平均线, color='b', linestyle=':') # 也可用plt.plot代替
plt.show()
#############


############# 画面和子图
画布 = plt.figure()
第一个 = 画布.add_subplot(221)
第二个 = 画布.add_subplot(222)
第三个 = 画布.add_subplot(223)
plt.plot(数据.班级, 数据.毛利率, label='毛利率', color='r', marker='*', ms=10)
第四个 = 画布.add_subplot(224)
plt.bar(数据.班级, 数据.销售量, color='r', label='销售量', alpha=0.6)
plt.show()
#############


############# 创建多个子图
布=plt.figure(num='画布名称',figsize=(12,13),dpi=200,facecolor='w') #facecolor背景色
plt.subplot(221) # 2行2列第一个图
plt.bar(数据.班级,数据.销售量)
plt.subplot(222)
plt.subplot(223)
plt.pie(数据.销售量,labels=tuple(数据.班级))
plt.subplot(224)
plt.plot(数据.班级,数据.毛利率)
plt.show()
           
布, 图 = plt.subplots(2,2)
图1 = 图[0,0]
图2 = 图[0,1]
图3 = 图[1,0]
图4 = 图[1,1]
图1.bar(数据.班级,数据.销售量)
图4.pie(x=数据.销售量,labels=tuple(数据.班级))
plt.show()
#############


############# 新增子区域
布 = plt.figure()
left,bottom,width,height=0.1, 0.1, 0.8, 0.8
图1 = 布.add_axes([left,bottom,width,height])
图1.bar(数据.班级,数据.销售量)
图1.set_title('销售量')

left,bottom,width,height=0.65, 0.6, 0.25, 0.25
图2 = 布.add_axes([left,bottom,width,height])
图2.plot(数据.班级,数据.毛利率)
图2.set_title('毛利率')
plt.show()
#############


############# 调整边框与子图间距
布.tight_layout() # 自动调整布局

# 手动调整布局
布, 图 = plt.subplots(2,2)
布.subplots_adjust(wspace=0.5,hspace=0.3,left=0.125,right=0.9,top=0.9,bottom=0.1)
plt.show()
#############


############# 组合图：柱形图+折线图
布 = plt.figure()
图1 = 布.add_subplot(111)
图1.bar(数据.班级, 数据.销售量, label='销售量')
图1.legend(loc='upper left')
图1.set_ylim([0,12500])
图2=图1.twinx()
图2.plot(数据.班级,数据.毛利率, color='r',label='毛利率')
图2.legend(loc='upper right')
plt.show()

# 实现百分比标签 （只需要添加一个%的话）
import matplotlib.ticker as mtick
图2=图1.twinx()
百分比标签 = mtick.FormatStrFormatter('%.2f%%')
图2.plot(数据.班级,数据.毛利率2, 'or-', color='r',label='毛利率') #毛利率38.25 -〉 38.25%
图2.yaxis.set_major_formatter(百分比标签)
for x, y in zip(数据.班级, 数据.毛利率2):
    plt.text(x,y,str(y)+'%',c='b', fontsize=20)
plt.show()

# 实现百分比标签 （乘以100再加上%的话）
import matplotlib.ticker as ticker
图2=图1.twinx()
图2.plot(数据.班级,数据.毛利率2, 'or-', color='r',label='毛利率')
自己设置百分比=ticker.PercentFormatter(1,2) # 1는 100%의미함, 2는 소수점 2자리
图2.yaxis.set_major_formatter(自己设置百分比)
图2.legend(loc='upper right')
图2.set_ylim([0,1])
for x,y in zip(数据.班级, 数据.毛利率):
    plt.text(x,y,str(round(y*100,2))+'%', c='b', fontsize=20)
plt.show()
#############


############# 坐标轴上面的日期格式
日期 = [d.strftime('%Y-%m-%d') for d in 数据.日期]
plt.plot(日期, 数据.销售)
plt.xticks(日期,rotation=45)   # plt.tight_layout()
plt.show()
#############


############# 网格线
plt.plot(数据.日期,数据.销售)
plt.grid(axis='x',color='r',linestyle=':',linewidth=3) # 不写axis='x'的话代表所有轴
plt.show()
#############


############# 散点图
# pd.options.display.max_columns=None 
# pd.options.display.max_rows=None 
plt.scatter(数据.身高,数据.体重,s=数据.身高,c=数据.身高,marker='o',alpha=0.5) # s=数据.身高 身高越高，气泡越大
plt.colorbar()
plt.show()

import numpy
import matplotlib.pyplot as plt
k=500
x=np.random.rand(k)
y=np.random.rand(k)
大小=np.random.rand(k)*50
颜色=np.arctan2(x,y)
plt.scatter(x,y,s=大小,c=颜色)
plt.colorbar()
plt.show()
#############


############# 直方图
plt.hist(数据.身高,bins=30,facecolor='b',edgecolor='w',alpha=0.6)
plt.show()
#############


############# 坐标轴
# 删除上面的轴和右边的轴，轴刻度倒过来
布,图 = plt.subplots(1,1)
图.spines['top'].set_color('none')
图.spines['right'].set_color('none')
图.spines['left'].set_color('g')
图.spines['bottom'].set_color('r')
轴 = plt.gca()
轴.invert_yaxis()
轴.invert_xaxis()
plt.show()
    
# 让x,y轴消失
布,图 = plt.subplots(1,1)
图.spines['top'].set_color('none')
图.spines['right'].set_color('none')
图.spines['left'].set_color('none')
图.spines['bottom'].set_color('none')
图.set_xticks([])   # 让刻度消失
图.set_yticks([])   # 让刻度消失
plt.show()
           
布,图 = plt.subplots(1,1)
图.spines['left'].set_color('none')
图.spines['bottom'].set_color('none')
图.spines['top'].set_color('r')
图.spines['right'].set_color('g')
图.xaxis.set_ticks_position('top')
图.yaxis.set_ticks_position('right')
plt.show()
        
# 对x轴上面的第二个数值进行放大，更改颜色
布,图 = plt.subplots(1,1)
图.plot(数据.序号,数据.身高)
plt.gca().get_xticklabels()[2].set(c='r',fontsize=30)
plt.show()
           

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as ticker
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
import matplot
布，图 = plt.subplots(1,1)
图.plot(数据.序号,数据.身高)
#plt.locator_params('x', nbins=5)   #将x轴分成5份
#plt.gca().locator_params('x',nbins=5)
#plt.gca().locator_params(nbins=5) #将x,y轴分成5份
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(7)) # x轴的刻度为7的倍数
#plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f')) # 保留小数点后两位
plt.show()
           
import matplotlib as mpl
plt.plot(数据.日期,数据.销售)
plt.gca().xaxis.set_major_formatter(mpl.dates.DateFormatter('%Y*%m*%d'))
plt.show()
          
plt.plot(数据.时间,数据.蔬菜)
#plt.gca().set_xlim([0,10])
plt.gca().set_ylim([0,30])
plt.gca().axis([0,10,0,30])   # [x轴最小值，最大值，y轴最小值,最大值]
plt.gca.set_ylim(bottom=-10)
plt.gca.set_xlim(left=5)   # right = 25
plt.show()
#############


############# 叠加区域图
plt.plot(数据.时间,数据.蔬菜)
plt.plot(数据.时间,数据.水果)
plt.fill_between(数据.时间,0,数据.蔬菜,facecolor='r',alpha=0.3) # 覆盖区域x轴, 覆盖区域下限，覆盖区域上限
plt.fill_between(数据.时间,0,数据.水果,facecolor='g',alpha=0.3) 
plt.show()
     
# 自定义区域进行high light显示
import numpy as np
import matplotlib.pyplot as plt
x = np.array([i for i in range(30)])
y = np.random.rand(30)
列表 = [[1,6],[10,12],[20,23],[26,28]]
plt.plot(x,y,'r')
for i in 列表:
    plt.fill_between(x[i[0]:i[1]],0,1,facecolor='r', alpha=0.3)
plt.show() 
#############


############# 极坐标
#plt.polar(极角,极轴)
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')   # 风格设置 灰色打底
plt.polar(0.25*np.pi,20,'go')  # 45度角，数据到20
plt.ylim(0,100)
plt.show()

# 角度 = np.array([0.25,0.75,1,1.5,0.25])
# 极轴 = [20,60,40,80,20]
# plt.polar(角度*np.pi,极轴,'ro-',alpha=0.25) 将几个点全部用线连接起来，为保证最后一个点也连上线，将第一个点的数值也添加到最后
# plt.fill(角度*np.pi,极轴,'r',alpha=0.25) 填充颜色
# plt.ylim(0,100)
# plt.show()
#############


############# 雷达图
数据 = pd.read_excel(path, index_col='姓名')
条件1 = "姓名=='A01'"
条件2 = "姓名=='A02'"
A01 = 数据.query(条件1)['分数']
A02 = 数据.query(条件2)['分数']
科目 = 数据.query(条件1)['科目']
角度 = np.linspace(0,2*np.pi,len(A01),endpoint=False) # linspace用于构建一个等差数列
#np.linspace(start,stop,num=50,endpoint=True)

A01 = np.concatenate((A01, [A01[0]]))
A02 = np.concatenate((A02, [A02[0]])) # 将第一个值也放在最后 使它连接上
科目 = np.concatenate((科目,[科目[0]]))
角度 = np.concatenate((角度,[角度[0]]))

plt.style.use('ggplot')
布 = plt.figure()
图 = 布.add_subplot(111,polar=True)
图.plot(角度,A01,'o-',linewidth=2,alpha=0.25,label='A01同学')
图.fill(角度,A01,'r',alpha=0.25)
图.plot(角度,A02,'o-',linewidth=2,alpha=0.25,label='A02同学')
图.fill(角度,A02,'b',alpha=0.25)
图.set_thetagrids(角度*180/np.pi,科目) # 设置标签（科目）
图.set_ylim(0,100)
plt.legend(loc='upper right')
plt.show()
#############


############# 标题及轴标签
布 = plt.figure()
plt.subplot(221)
plt.plot(['A','B','C'],[1,2,3],'ro-')
字典 = dict(facecolor='yellow',pad=5,alpha=0.2)  # 给轴标签加上一个框,pad代表框框大小
plt.xlabel('李平平',bbox=字典)
plt.subplot(222)
plt.subplot(223)
plt.subplot(224)
plt.suptitle("孙兴华",fontsize=20,fontweight='bold',color='r') # 添加布标题
plt.subplots_adjust(left=0.2,top=0.8,wspace=0.8,hspace=0.8,bottom=0.1)
plt.show()
#############


############# 样式
# 折线样式
import matplotlib.pyplot as plt
x = ['A','B','C','D','E','F']
y=[1,10,7,5,11,6]
plt.plot(x,y,drawstyle='steps') # steps-pre,steps-mid,steps-post
plt.show()

# 画布样式
print(plt.style.available) # 打印所有样式
plt.style.use('ggplot') # 使用样式
plt.subplots()
plt.show()
#############


############# 填充
plt.axhline(y=0.2,linewidth=8,c='r') # linewidth=30 调整线粗细
plt.axvline(x=0.4) # 划竖线
plt.axhline(y=0.5,xmin=0.2,xmax=0.6) # 只显示一段
plt.axhspan(1,1.3,facecolor='y',alpha=0.5) # 从y轴1到1.3进行颜色填充
plt.axvspan(1,1.3,facecolor='b',alpha=0.5)
plt.axis([-1,2,-1,2]) # 设置坐标轴x，y轴的范围
plt.show()
#############


############# 交叉及填充
布,图 = plt.subplots()
图.plot(x,y1,x,y2,color='black')
图.fill_between(x,y1,y2,where=y2>y1,facecolor='g')
图.fill_between(x,y1,y2,where=y2<y1,facecolor='r')
plt.show()
#############


############# 文本注释
# 设置文本及文本位置，并添加箭头
import matplotlib.pyplot as plt
plt.plot(['A','B','C'],[5,2,3],'ro-')
字典 = dict(width=1,headwidth=5,facecolor='r',shrink=0.05)
plt.annotate('sxh',xy=('B',2),xytext=("B",2.5),arrowprops=字典) # xytext设置文本位置
plt.show()

# 设置文本及文本边框
plt.plot(['A','B','C'],[5,2,3],'ro-')
边框 = dict(boxstyle='sawtooth',fc='0.8',ec='r') # facecolor, edgecolor
plt.text('B',2,'sxh',size=20,bbox=边框)
plt.show()

# 设置箭头方式
plt.plot(['A','B','C'],[5,2,3],'ro-')
字典 = dict(arrowstyle='->',connectionstyle='arc') # connectionstyle 设置箭头方式
plt.annotate('sxh',xy=('B',2),xytext=('C',5),arrowprops=字典)
plt.show()
#############


############# 瀑布图
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel(path)
列表 = np.arange(len(数据.金额),dtype=np.float64)
下面的距离 = 0
for i in 数据.金额.index:
    x = 列表[i]
    y = 数据.金额[i]
    if 数据.金额[i] >= 0:
         盈利 = plt.bar(x,y,0.8,align='center',bottom=下面的距离,label='盈利',color='r')
    else:
         亏损 = plt.bar(x,y,0.8,align='center',bottom=下面的距离,label='亏损',color='g')
    下面的距离+=y
    x += 0.8

plt.gca().yaxis.grid(True,linestyle='--',color='grey',alpha=0.25)
日期 = [d.strftime('%Y-%m-%d')for d in 数据.日期]
plt.xticks(np.arange(len(数据.金额)),日期,rotation=45)
plt.show()
#############


############# 树状图
import matplotlib.pyplot as plt
import squarify
import pandas as pd
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel(path)
自定义颜色 = ['r','y','b','g','yellow','cyan','coral']
图 = squarify.plot(sizes=数据.销售数量,label=数据.名称,color=自定义颜色,value=数据.销售数量,edgecolor='white',linewidth=3,text_kwargs={'fontsize':20})
plt.axis('off') # 删除坐标轴
图.set_title('销售情况',fontdict={'fontsize':20})
plt.show()
#############


############# 玫瑰图
data = pd.read_excel(path)
颜色 = ['b','gold','darkviolet','turquoise','r','g','grey','c','m','y','k','darkorange','lightgreen']
角度 = np.linspace(0,2*np.pi,len(数据.业绩,endpoint=False)
图 = plt.axes(polar=True)
图.set_theta_zero_location('N') # 将上面设为北
#图.set_theta_direction(-1) # 180度旋转
业绩 = np.concatenate((数据.业绩,[数据.业绩[0]]))
角度 = np.concatenate((角度,[角度[0]]))
姓名 = np.concatenate((数据.姓名,[数据.姓名[0]]))
plt.bar(角度,业绩,width=0.33,color=颜色)
plt.bar(角度,height=130,width=0.33,color='white')
for 角度,业绩,姓名 in zip(角度,业绩,姓名):
    plt.text(角度+0.03,业绩+100,str(姓名))
plt.gca().set_axis_off()
plt.show()
#############
