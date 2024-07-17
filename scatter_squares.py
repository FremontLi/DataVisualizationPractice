import matplotlib.pylab as plt

x_values=range(1,5000)
y_values=[x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,s=10)

# 设置图标题并给坐标轴加上标签
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0,5000,0,100_000_000_000])
ax.ticklabel_format(style='plain')

# plt.savefig('square_plt.png',bbox_inches='tight')
plt.show()