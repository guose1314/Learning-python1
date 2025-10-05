import requests
from requests.exceptions import RequestException
import tkinter as tk
import pygame
class Translate():
    def __init__(self):
        self.window = tk.Tk()  #创建window窗口
        self.window.title("Tk翻译器")  # 定义窗口名称
        self.window.resizable(0,0)  # 禁止调整窗口大小
        self.input = tk.Entry(self.window, width=80)  # 创建一个输入框,并设置尺寸
        self.info = tk.Text(self.window, height=18)   # 创建一个文本展示框，并设置尺寸
        # 添加一个按钮，用于触发翻译功能
        self.t_button = tk.Button(self.window, text='翻译', relief=tk.RAISED, width=8, height=3, command=self.fanyi)
        self.c_button2 = tk.Button(self.window, text='清空', relief=tk.RAISED,width=8, height=3, command=self.cle)
        # 添加一张图标

    def gui_arrang(self):
        """完成页面元素布局，设置各部件的位置"""
        self.input.grid(row=0,sticky="W",padx=1)
        self.info.grid(row=1)
        self.t_button.grid(row=0,column=1,padx=2)
        self.c_button2.grid(row=0,column=3,padx=2)

    def fanyi(self):
        """定义一个函数，完成翻译功能"""
        original_str = self.input.get()  # 定义一个变量，用来接收输入框输入的值
        data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': original_str  # 将输入框输入的值，赋给接口参数
        }
        url = "http://fanyi.youdao.com/translate"
        try:
            r = requests.get(url, params=data)
            if r.status_code == 200:
                result = r.json()
                translate_result = result['translateResult'][0][0]["tgt"]
                self.info.delete(1.0, "end")  # 输出翻译内容前，先清空输出框的内容
                self.info.insert('end',translate_result)  # 将翻译结果添加到输出框中
        except:
            self.info.delete(1.0,"end")  # 从第一行清除到最后一行
            self.input.delete(0,"end")
            self.info.insert('end', "error")
    def cle(self):
        """定义一个函数，用于清空输出框的内容"""
        self.info.delete(1.0,"end")  # 从第一行清除到最后一行
        self.input.delete(0,"end")

def main():
    t = Translate()
    t.gui_arrang()
    tk.mainloop()

if __name__ == '__main__':
    main()
