import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.gridspec as gridspec


'''
plt.saving()将输出图形存储为文件，默认png格式，
可通过dip修改输出质量，
例如dip=600表示每一英寸空间中包含600个像素点
'''
#图二折线图
plt.subplot(4,4,2)
plt.plot([0, 2, 4, 6, 8],[3, 1, 4, 5, 2])

#plt.plot(x,y)当有两个以上参数时，按照x轴和y轴顺序绘制数据点

plt.ylabel("Grade")
plt.axis([-1, 10, 0, 6])
plt.show()


'''
pyplot分隔绘图区域的办法
plt.subplot(nrows,ncols,plot_number)
例如：plt.subplot(3,2,4)表示将该区域划分为横二纵三的六个区域，
当前绘图区域为六个中的第四个
使用plt.subplot(324)也能得到同样的效果
'''

