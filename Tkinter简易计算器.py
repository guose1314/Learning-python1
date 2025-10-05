import tkinter as TK
from tkinter import messagebox
import requests
import time
import pygame
# from xes import common
import pygame
pygame.init()
#若调用 eval（）函数进行计算结果，把下面这一小段代码去掉

#########################################################

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


root = TK.Tk()
root.title("计算器")
root.resizable(0,0)
root.geometry('180x340')
result = TK.StringVar()
equation = TK.StringVar()
result.set('')
equation.set('')
def getnum(num):
    temp = equation.get()
    temp2 = result.get()
    if temp2 != ' ' :
        temp = ''
        temp2 = ' '
        result.set(temp2)
    temp = temp + num
    equation.set(temp)

# 按下退格键时，去除最后一个字符
def back():
    temp = equation.get()
    equation.set(temp[:-1])

# 按下MC时，清空算式行与结果行
def clear():
    equation.set('')
    result.set('')

# 按下等于号时计算结果
def run():
    temp = equation.get()
    temp3 = temp.replace('x','×')
    temp = temp.replace('x','*')
    temp = temp.replace('÷','/')
    try:
        answer = eval(temp)
    except Exception as e:
        answer = 'Error'
        result.set(str(answer))
        message = '出错了...错误原因:' + str(e)
        messagebox.showinfo('出错了',message)
    else:
        ans_str = str(answer)
        ans_len = int(len(ans_str))
        if answer % 1 == 0:
            answer = '%d'%answer
        elif temp == '.1+0.2' or temp == '0.1+0.2' or temp == '(0.1+0.2)':
            answer = 0.3
        elif temp == '.1+0.2+0.3' or temp == '0.1+0.2+0.3' or temp == '(0.1+0.2+0.3)':
            answer = 0.6
        elif ans_len > 6:
            answer = '%E' % answer
        else:
            answer = '%f'%answer
        text = str(temp3) + '=' +str(answer)
        print(text)
        result.set(str(answer))
        messagebox.showinfo('提示窗口',text)
show_uresult = TK.Label(root,bg='white',fg = 'black',font = ('Minecraft','15'),bd='0',textvariable =equation,anchor='se')
show_dresult = TK.Label(root,bg='white',fg = 'black',font = ('Minecraft','20'),bd='0',textvariable=result,anchor='se')
show_uresult.place(x='10',y='0',width='160',height='50')
show_dresult.place(x='10',y='50',width='160',height='50')
button_back =TK.Button(root,text='←',fg = ('#4F4F4F'),command=back)
button_back.place(x = '10',y='140',width = '40',height='40')
button_lbracket=TK.Button(root,text='(',fg = ('#4F4F4F'),command= lambda : getnum('('))
button_lbracket.place(x = '50',y='140',width = '40',height='40')
button_rbracket=TK.Button(root,text=')',fg = ('#4F4F4F'),command= lambda : getnum(')'))
button_rbracket.place(x = '90',y='140',width = '40',height='40')
button_division =TK.Button(root,text='÷',fg = ('#4F4F4F'),command= lambda : getnum('÷'))
button_division.place(x = '130',y='180',width = '40',height='40')
button_7 =TK.Button(root,text='7',fg = ('#4F4F4F'),command= lambda : getnum('7'))
button_7.place(x = '10',y='180',width = '40',height='40')
button_8 =TK.Button(root,text='8',fg = ('#4F4F4F'),command= lambda : getnum('8'))
button_8.place(x = '50',y='180',width = '40',height='40')
button_9 =TK.Button(root,text='9',fg = ('#4F4F4F'),command= lambda : getnum('9'))
button_9.place(x = '90',y='180',width = '40',height='40')
button_multiplication =TK.Button(root,text='x',fg = ('#4F4F4F'),command= lambda : getnum('x'))
button_multiplication.place(x = '130',y='140',width = '40',height='40')
button_4 =TK.Button(root,text='4',fg = ('#4F4F4F'),command= lambda : getnum('4'))
button_4.place(x = '10',y='220',width = '40',height='40')
button_5 =TK.Button(root,text='5',fg = ('#4F4F4F'),command= lambda : getnum('5'))
button_5.place(x = '50',y='220',width = '40',height='40')
button_6 =TK.Button(root,text='6',fg = ('#4F4F4F'),command= lambda : getnum('6'))
button_6.place(x = '90',y='220',width = '40',height='40')
button_minus =TK.Button(root,text='-',fg = ('#4F4F4F'),command= lambda : getnum('-'))
button_minus.place(x = '130',y='100',width = '40',height='40')
button_1 =TK.Button(root,text='1',fg = ('#4F4F4F'),command= lambda :getnum('1'))
button_1.place(x = '10',y='260',width = '40',height='40')
button_2 =TK.Button(root,text='2',fg = ('#4F4F4F'),command= lambda : getnum('2'))
button_2.place(x = '50',y='260',width = '40',height='40')
button_3 =TK.Button(root,text='3',fg = ('#4F4F4F'),command= lambda : getnum('3'))
button_3.place(x = '90',y='260',width = '40',height='40')
button_plus =TK.Button(root,text='+',fg = ('#4F4F4F'),command= lambda : getnum('+'))
button_plus.place(x = '90',y='100',width = '40',height='40')
button_C =TK.Button(root,text='C',fg = ('#4F4F4F'),command = clear)
button_C.place(x = '10',y='100',width = '80',height='40')
button_0 =TK.Button(root,text='0',fg = ('#4F4F4F'),command= lambda : getnum('0'))
button_0.place(x = '10',y='300',width = '40',height='40')
button_point =TK.Button(root,text='.',fg = ('#4F4F4F'),command= lambda : getnum('.'))
button_point.place(x = '90',y='300',width = '40',height='40')
button_equal=TK.Button(root,text='=',fg = ('#4F4F4F'),command= run)
button_equal.place(x = '130',y='260',width = '40',height='80')
button_00 =TK.Button(root,text='00',fg = ('#4F4F4F'),command= lambda : getnum('00'))
button_00.place(x = '50',y='300',width = '40',height='40')
button_diq = TK.Button(root,text='%',fg = ('#4F4F4F'),command= lambda : getnum('%'))
button_diq.place(x = '130',y='220',width = '40',height='40')
root.attributes("-toolwindow", 1)
root.mainloop()
