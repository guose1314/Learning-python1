import socket
import _thread
class Server:
    buffer_size = 1024
    client_addr=()
    server=None
    conn=None
    global is_chating #监听器
    def __init__(self,host :str,port :int):
        ip_port=(host,port)
        self.is_chating=False
        try:
            # 声明套接字类型 AF_INET 表示用于网络通信  socket.SOCK_STREAM   tcp协议，基于流式的协议
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 对socket的配置使用IP与端口号的配置
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # 绑定ip与端口
            self.server.bind(ip_port)
            # 设置最大连接多少个客户端
            self.server.listen(5)
            print('服务器已建立,正在等待连接')
            self.conn,self.client_addr=self.server.accept()
            print('已建立来自'+self.client_addr[0]+'的连接,可以发送或接受数据')

            # 发送问候
            welcome='你好 欢迎进入服务器'
            self.send(welcome)
        except Exception as e:
            print(e.with_traceback())
            exit(0)
        except :
            print("连接失败")
    def send(self,msg :str):
        try:
            if msg =='':
                print('发送消息不准为空')
                return
            self.conn.send(msg.encode('utf-8'))
        except ConnectionResetError as s:
            print('发生错误 类型:'+s.errno)
        except:
            pass
    def recv(self)->str:
        try:
            return self.conn.recv(self.buffer_size).decode('utf-8')
        except ConnectionResetError as s:
            print('发生错误 类型:' + s.errno)
        except:
            print("发生其他错误")
    def close(self):
        self.conn.close()
        self.server.close()

    def cycle_Send(self):
        while 1:
            if self.is_chating == False:
                break
            msg=input('')
            if msg=='':
                continue
            self.send(msg)
            print(self.right(msg))
            if msg=="bye" or msg =='quit' or msg=="再见":
                break
        self.is_chating = False
    def cycle_Recv(self):
        while 1:
            if self.is_chating == False:
                break
            msg=self.recv()
            if msg=='': #由于发送的消息已经经过判断不为空处理 如果接受到的数据为空 说明连接已断开
                print('连接已中断')
                self.is_chating = False
                break
            print(self.left(msg))
            if msg=="bye" or msg =='quit' or msg == "再见":
                break
        self.is_chating = False

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

    def interaction(self): # 创建两个线程 形成交互式聊天窗口
        try:
            print('已经进入聊天室发送\'bye\'或\'再见\'推出聊天')
            _thread.start_new_thread(self.cycle_Send,())
            _thread.start_new_thread(self.cycle_Recv,())
        except:
            print("失败")
def menu():
    print('------网络通信服务端------\n')
    print("1.开启服务器,准备接受会话\n2.关闭连接\n3.退出程序")
if __name__ == '__main__':
    #print('1.发送数据')
    while 1:
        menu()
        a = input()
        if a == '1':
            server = Server('127.0.0.1', 7777)
            server.is_chating = True
            server.interaction()
            while 1: #阻塞主进程,防止主进程结束
                if server.is_chating == False:
                    print('聊天已结束')
                    break
                pass
        elif a == '2':
            try:
                server.close()
                del server
                print("连接已关闭,请重新建立连接")
            except Exception as e:
                print("错误代码:"+e)
        elif a == '3':
            exit(0)
