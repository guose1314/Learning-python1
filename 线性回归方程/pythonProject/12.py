# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:03:49 2019

@author: lenovo
"""

import xlrd
import numpy as np
import matplotlib.pyplot as plt

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

#从excel文件中读取数据
def read(file):
	wb = xlrd.open_workbook(filename=file)#打开文件
	sheet = wb.sheet_by_index(0)#通过索引获取表格
	rows = sheet.nrows # 获取行数
	all_content = []        #存放读取的数据
	for j in range(0, 2):       #取第1~第2列对的数据
		temp = []
		for i in range(1,rows) :
			cell = sheet.cell_value(i, j)   #获取数据 
			temp.append(cell)           
		all_content.append(temp)    #按列添加到结果集中
		temp = []
	return np.array(all_content)    #返回读取的数据
#获得拟合函数并绘制图象
def temp1(datas):
	x = datas[0]        #获取自变量x
	y = datas[1]        #获取因变量y
	n = np.size(answer1, axis = 1)  #获取有多少个自变量，axis=1代表获取矩阵的列数
	#根据公式计算k
	k = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(np.power(x,2)) - np.sum(x) * np.sum(x))   
	#根据公式计算b
	b = (np.sum(np.power(x,2)) * np.sum(y) -np.sum(x) * np.sum(x*y)) / (n*np.sum(np.power(x,2)) - np.sum(x) * np.sum(x))
	las = k*x + b       #根据公式得到拟合函数
	fig = plt.figure()  #获得figure对象
	ax1 = fig.add_subplot(1,1,1)    #添加一个图纸
	ax1.set_xlim([min(x)-0.5, max(x)+0.5])      #设置x轴刻度
	ax1.set_ylim([min(y) -0.5, max(y) +0.5])    #设置y轴刻度
	plt.plot(x,las,'k',label='拟合函数')    #画出拟合函数
	plt.plot(x,y,'o',label = '样本数据')    #画出样本数据
	plt.plot(x,y,'o',label='k:'+str(k))  # 画出样本数据
	plt.plot(x,y,'o',label='b:'+str(b))  # 画出样本数据
	plt.grid()  #添加网格线
	ax1.legend(loc = 'best')    #设置图例的位置为最佳best
	plt.show()
	return [k,b]    #返回k和b
#通过计算拟合优度评价拟合函数
def judge(datas,k,b):
	x = datas[0]    #获取自变量x
	y = datas[1]    #获取自变量y
	z = k * x + b   #得到拟合函数
	SST = np.sum(np.power(y - np.average(y),2))     #根据公式计算SST
	SSE = np.sum(np.power(y - z, 2))                #根据公式计算SSE
	SSR = np.sum(np.power(z - np.average(y),2))     #根据公式计算SSR
	R_2 = SSR / SST             #得到R_2
	print('k = ',k)
	print('b = ',b)
	print('SST = ',SST)
	print('SSE = ',SSE)
	print('SSR = ',SSR)
	print('R_2 = ',R_2)
	
answer1 = read('E:\\13.xlsx')
answer2 = temp1(answer1)
judge(answer1,answer2[0],answer2[1])
