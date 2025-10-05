import socket
import _thread
class Client:
    bufSize=1024
    client =None
    global is_chating # 监听器
    def __init__(self,ip :str,port :int):
        ip_port=(ip,port)
        self.is_chating=False
        try:
            print("正在尝试连接服务器....")
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(ip_port)
        except ConnectionResetError as e:
            print("错误代码:"+e.errno)
            exit(0)
        except socket.timeout:
            print("连接超时")
            exit(0)
        print("连接成功,可以发送数据")
        
    def send(self,msg:str):
        try:
            if msg =='':
                print('发送消息不准为空')
                return
            self.client.send(msg.encode('utf-8'))
        except ConnectionResetError as e:
             print(e.strerror)
        except:
            pass

    def recv(self)->str:
        try:
            return self.client.recv(self.bufSize).decode('utf-8')
        except ConnectionResetError as e:
            print("发送失败,网络错误:"+str(e.strerror))
            exit(0)
        except:
            pass
    def close(self):
        self.client.close()

    def cycle_Send(self):
        while 1:
            if self.is_chating == False:
                break
            msg=input("")
            if msg=='':
                continue
            self.send(msg)
            print(self.right(msg))
            if msg=="bye" or msg =='quit' or msg=="再见" :
                break
        self.is_chating = False
    def cycle_Recv(self):
        while 1:
            if self.is_chating==False:
                break
            msg=self.recv()
            if msg=='': # 由于发送的消息已经经过判断不为空处理 如果接受到的数据为空 说明连接已断开
                print('连接已中断')
                self.is_chating = False
                break
            print(self.left(msg))
            if msg=="bye" or msg =='quit' or msg == "再见":
                break
        self.is_chating = False
    def interaction(self): # 创建两个线程 形成交互式聊天窗口
        try:
            print('已经进入聊天室发送\'bye\'或\'再见\'推出聊天')
            _thread.start_new_thread(self.cycle_Send,())
            _thread.start_new_thread(self.cycle_Recv,())
        except:
            print("失败")

    def left(slef,msg) -> str:
        try:
            chat = '<|' + msg + '|\n'
            return chat
        except:
            pass
    def right(slef,msg) -> str:
        try:
            chat = '|' + msg + '|>\n'
            return chat.rjust(32)
        except:
            pass

def menu():
    print('------网络通信客户端------\n')
    print("1.建立与服务器的连接,并开始对话\n2.关闭连接\n3.退出程序")
if __name__ == '__main__':
    #print('1.发送数据')
    while 1:
        menu()
        a=input()
        if a=='1':
            client=Client('127.0.0.1',7777)
            client.is_chating = True
            client.interaction()
            while 1:# 阻塞主进程,防止主进程结束
                if client.is_chating == False:
                    print('聊天已结束')
                    break
                pass
        elif a=='2':
            try:
                client.close()
                del client
                print('连接已关闭,请重新建立连接')
            except Exception as e:
                print(e)
        elif a=='3':
            exit(0)