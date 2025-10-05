##编制高斯列主元消去法程序，并计算
import numpy as np
#读取txt并存储位数组
def readtxt(t):
    with open(t,'r') as f:
        lines = f.readlines()
        f.close()
        headings = lines[0].replace('\n','').split(',')#表头
        m = len(lines)# 大小 m行 x n列
        n = len(headings)
        data=np.zeros(shape=(m,n))
        for i in range(m):
            for j in range(n):
                data[i][j]=float(lines[i].replace('\n','').split(',')[j])

        #datab=np.array(datab).transpose()
        #数组分列
        A=data[:,0:4]
        #A=np.mat(A) #数组转矩阵
        b=data[:,4]
        #b=np.mat(b)
        b = np.transpose(b) #矩阵转置
        #B=np.transpose(B)
        return A,b

#矩阵运算
def swap(a, b, k, n):           # 找到主元并交换，这仅是一个仅用来交换的函数
    ans = 0
    for i in range(k, n):
        if ans < np.fabs(a[i][k]):    #fabs是绝对值，将a中绝对值最大的找出来
            ans = a[i][k]
            maxn = i
    a[[k, maxn], :] = a[[maxn, k], :]     #交换
    b[k], b[maxn] = b[maxn], b[k]

#主算法
def gauss(a, b):
    cout = 0                         #定义计算次数
    m, n = a.shape                  #矩阵a的行数和列数
    if ( m < n ):
        print("There is a 解空间。")#保证方程个数大于未知数个数
    else:
        l = np.zeros((n,n))
        for i in range(n):
            # 限制条件
            if(a[i][i] == 0):
                print("no answer")
        # j表示列
        for k in range(n - 1):          # k表示第一层循环，(0，n-1)行
            swap(a, b, k, n)            #在每次计算前，找到最大主元，进行换行
            for i in range(k + 1, n):   # i表示第二层循环,(k+1,n)行,计算该行消元的系数
                l[i][k] = a[i][k] / a[k][k]     #计算
                cout += 1
                for j in range(m):      # j表示列，对每一列进行运算
                    a[i][j] = a[i][j] - l[i][k] * a[k][j]
                    cout += 1
                b[i] = b[i] - l[i][k] * b[k]
        # 回代求出方程解
        x = np.zeros(n)
        x[n - 1] = b[n - 1] / a[n - 1][n - 1] #先算最后一位的x解

        for i in range(n - 2, -1, -1):      #依次回代倒着算每一个解
            for j in range(i + 1, n):
                b[i] -= a[i][j] * x[j]
                               #自增自减
            x[i] = b[i] / a[i][i]
            #x=np.mat(x)
            #x=np.transpose(x)
        for i in range(n):
            print("x" + str(i + 1) + " = ", x[i])
        print("x" " = ", x)
        #print("计算次数","=",cout) #计算次数

if __name__ == '__main__':      #当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
    A, b = readtxt('习题4-1.txt')
    x=gauss(A, b)
