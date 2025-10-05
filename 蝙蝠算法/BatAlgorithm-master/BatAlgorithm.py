import random 
import numpy as np

class BatAlgorithm():
    """
    蝙蝠算法
    """
    def __init__(self, D, NP, N_Gen, A, r, Qmin, Qmax, Lower, Upper, Alpha,Beita,function):
        self.D = D  #问题的维度
        self.NP = NP  #种群的数量
        self.N_Gen = N_Gen  #算法的迭代次数
        self.A = A  #蝙蝠的响度
        self.r_init = r  #脉冲频率
        self.Qmin = Qmin  #最小频率
        self.Qmax = Qmax  #最大频率
        self.Lower = Lower  #小值边界
        self.Upper = Upper  #大值边界
        self.Alpha=Alpha#响度衰减系数
        self.Beita=Beita#
        self.f_min = 0.0  #最小值
        
        self.Lb = [0] * self.D  #定义域下边界
        self.Ub = [0] * self.D  #定义域上边界
        self.Q = [0] * self.NP  #频率

        self.v = [[0 for i in range(self.D)] for j in range(self.NP)]  #变异的速度
        self.Sol = [[0 for i in range(self.D)] for j in range(self.NP)]  #种群的数量
        self.Fitness = [0] * self.NP  #适应值
        self.best = [0] * self.D  #存储的最优解
        self.Fun = function


    def best_bat(self):
        """
        找出值域中的最优解
        :return:
        """
        i = 0
        j = 0
        for i in range(self.NP):
            if self.Fitness[i] < self.Fitness[j]:
                j = i
        for i in range(self.D):
            self.best[i] = self.Sol[j][i]
        self.f_min = self.Fitness[j]

    def init_bat(self):
        """
        初始化蝙蝠种群
        :return:
        """
        for i in range(self.D):
            self.Lb[i] = self.Lower
            self.Ub[i] = self.Upper

        for i in range(self.NP):
            self.Q[i] = 0
            for j in range(self.D):
                rnd = np.random.uniform(0, 1)
                self.v[i][j] = 0.0
                self.Sol[i][j] = self.Lb[j] + (self.Ub[j] - self.Lb[j]) * rnd
            self.Fitness[i] = self.Fun(self.D, self.Sol[i])
        self.best_bat()

    def simplebounds(self, val, lower, upper):
        """
        查询值
        :param val:
        :param lower:
        :param upper:
        :return:
        """
        if val < lower:
            val = lower
        elif val > upper:
            val = upper
        return val

    def move_bat(self):
        S = [[0.0 for i in range(self.D)] for j in range(self.NP)]

        self.init_bat()
        r=self.r_init
        for t in range(self.N_Gen):
            for i in range(self.NP):
                rnd = np.random.uniform(0, 1)
                self.Q[i] = self.Qmin + (self.Qmax - self.Qmin) * rnd
                for j in range(self.D):
                    self.v[i][j] = self.v[i][j] + (self.best[j]-self.Sol[i][j]) * self.Q[i]
                    S[i][j] = self.Sol[i][j] + self.v[i][j]
                    S[i][j] = self.simplebounds(S[i][j], self.Lb[j],self.Ub[j])

                rnd = np.random.random_sample()
                if rnd > r:
                    for j in range(self.D):
                        S[i][j] = self.best[j] + 0.001 * random.gauss(0, 1)
                        S[i][j] = self.simplebounds(S[i][j], self.Lb[j],
                                                self.Ub[j])
                        
                Fnew = self.Fun(self.D, S[i])
                rnd = np.random.random_sample()

                if (Fnew <= self.Fitness[i]) and (rnd < self.A):
                    for j in range(self.D):
                        self.Sol[i][j] = S[i][j]
                    self.Fitness[i] = Fnew
                if Fnew <= self.f_min:#最优值的替换
                    for j in range(self.D):
                        self.best[j] = S[i][j]
                    self.f_min = Fnew
            self.A=self.A*self.Alpha
            r=self.r_init*(1-np.power(np.e,-t*self.Beita))
            if t%200==0:
                print('f_min:',self.f_min)
        print(self.f_min)
