# 柱状图
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


# 条形图
# 分组柱状图
# 添加数据标签
# 叠加柱状图
# 叠加条形图
# 饼图
# 3D饼图
# 折线图
# 平均线
# 画面和子图
# 创建多个子图
# 新增子区域
# 调整边框与子图间距
# 组合图：柱形图+折线图
# 坐标轴上面的日期格式
# 网格线
# 散点图
# 直方图
# 坐标轴
# 叠加区域图
# 极坐标
# 雷达图
# 标题及轴标签
# 样式
# 填充
# 交叉及填充
# 文本注释
# 瀑布图
# 树状图
# 玫瑰图
