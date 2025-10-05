import numpy as np

class emg_processing():
    # 提取活动段
    def get_act(data,qua):
        semg = np.array(data)
        semg = semg.transpose()
        semg = np.maximum(semg, -semg)
        semg = semg.mean(axis=1)
        jg_flag = 0
        act_flag = 0
        yangben_flag = 0
        sample_num = []
        window_len = 40
        act_data = [[]]
        qua_data = [[]]
        for i in range(int(len(semg)/window_len)):
            temp = np.array(semg[i*window_len:(i+1)*window_len])
            if temp.mean() >= 2.4:
                # print('data is act')
                act_flag = 1
                jg_flag = 0
                for j in range(8):
                    act_data[yangben_flag].extend(data[j][i * window_len:(i+1) * window_len])
                for k in range(4):
                    qua_data[yangben_flag].extend(qua[k][i * 3:(i+1) * 3])
            else:
                # print('data is rest')
                if act_flag == 1:
                    if jg_flag < 3:
                        for j in range(8):
                            act_data[yangben_flag].extend(data[j][i * window_len:(i + 1) * window_len])
                        for k in range(4):
                            qua_data[yangben_flag].extend(qua[k][i * 3:(i+1) * 3])
                        jg_flag += 1
                    else:
                        if len(act_data[yangben_flag]) > 10*8*window_len:
                            yangben_flag += 1
                            act_data.append([])
                            qua_data.append([])
                        act_flag = 0
                        jg_flag = 0

        act_data=act_data[0:-1]
        qua_data=qua_data[0:-1]
        for i in range(len(act_data)):
            sample_num.append(int(len(act_data[i])/8/window_len))
        print('样本个数：', len(act_data))
        print('样本窗数：', sample_num)
        # print(act_data)
        return act_data, sample_num,qua_data

    # 数据配齐
    def data_normalization(self,act_data, mean_window_num):
        # 将返回的每个样本窗数，带标签的rawdata，进行数据配齐
        feature = [ ]
        label = [ ]
        print('actdata:',np.array(act_data).shape)
        for i in range(len(act_data)):
            #print(len(act_data[i]))
            for j in range(len(act_data[i])):
                data = []
                data_1 = []
                for x in range(64):
                    data.append([])
                for y in range(int(len(act_data[i][j])/1920)):
                    data_1.append(act_data[i][j][1920*y:1920*(y+1)])
                    for k in range(64):
                        data[k].extend(data_1[y][k*30:(k+1)*30])
                # print('data:',np.array(data).shape)
                # for m in range(int(len(data)/64)):
                #     data_1.append(data[m*64:(m+1)*64])
                window_len = len(act_data[i][j])/64/int(mean_window_num)
                # print(window_len)
                # data_2=[]
                # for m in range(64):
                #     data_2.append([])
                data_3=[]
                for n in range(int(mean_window_num)):
                    data_2 = []
                    for y in range(64):
                        data_2.append(data[y][int(n)*int(window_len):(int(n)+1)*int(window_len)])
                    # nontran = np.log10(np.square(np.array(data_2))+1e-5)
                    temp1 = self.get_PSD(data_2)
                    # temp2 = self.get_PSD(nontran.tolist())
                    # temp = np.multiply(-2, np.divide((np.multiply(temp1, temp2)), (np.square(temp1) + np.square(temp2))))
                    # temp = np.nan_to_num(temp)
                    data_3.append(temp1)
                feature.append(data_3)
                label.append(i)
        feature = np.array(feature).swapaxes(1,2)
        # print(feature[5][5][5])
        print('feature:', feature.shape)
        print('label:', np.array(label).shape)
        return feature, label

    # TD-PSD特征提取
    def get_PSD(self,act_data):
        # print('act_data',act_data)
        # for i in range(len(act_data)):
        #     print(len(act_data[i]))
        #     act_data[i] = np.array(act_data[i])
        data = np.array(act_data)
        # print('data',data.shape)
        parameter = 0.1
        firstDeriv = np.diff(data, n=1)
        secDeriv = np.diff(data, n=2)
        # print(firstDeriv.shape)
        # print(secDeriv.shape)
        m0 = np.sqrt(np.sum(np.square(data), axis=1)) / parameter
        m2 = np.sqrt(np.sum(np.square(firstDeriv), axis=1) / len(data[0])) / parameter
        m4 = np.sqrt(np.sum(np.square(secDeriv), axis=1) / len(data[0])) / parameter
        f1 = np.log10(m0)
        f2 = np.log10(m0 - m2)
        f3 = np.log10(m0 - m4)
        # deno = np.sqrt(m0 - m2) * np.sqrt(m0 - m4)
        # f4 = np.log10(m0 / deno)
        # deno1 = np.sqrt(m0 * m4)
        # f5 = np.log10(m2 / deno1)
        # f6 = np.log10(np.sum(abs(firstDeriv), axis=1) / np.sum(abs(secDeriv), axis=1))

        # # mav:f0
        # f0=[]
        # for i in range(64):
        #     for j in range(len(data[i])):
        #         data[i][j] = abs(data[i][j])
        #     f0.append(data[i].mean())
        #
        # # wl
        # WL = 0
        # f7 = []
        # for i in range(64):
        #     wl = list(map(lambda x: x[0] - x[1], zip(data[i][1:len(data[i]) - 1], data[i][0:len(data[i]) - 2])))
        #     for j in range(len(wl)):
        #         WL += abs(wl[j])
        #     f7.append(WL)
        #     WL = 0

        # #ssc
        # ssc = 0
        # f8 = []
        # thre = np.std(data, ddof=1) * 0.05  # 待改进（每通道标准差）
        # for j in range(64):
        #     for k in range(2, len(data[j])):
        #         if (data[j][k - 1] - data[j][k - 2]) * (data[j][k - 1] - data[j][k]) < 0 and (
        #                 abs(data[j][k - 1] - data[j][k - 2]) > thre or (data[j][k - 1] - data[j][k]) > thre):
        #             ssc += 1
        #     f8.append(ssc)
        #     ssc = 0

        # # zc
        # zerocrossings = 0
        # f9 = []
        # thre = np.std(data, ddof=1) * 0.05  # 待改进（每通道标准差）
        # for j in range(64):
        #     for k in range(1, len(data[j])):
        #         if (data[j][k - 1]) * (data[j][k]) < 0 and abs(data[j][k] - data[j][k - 1]) > thre:
        #             zerocrossings += 1
        #     f9.append(zerocrossings)
        #     zerocrossings = 0


        feature = np.transpose(np.array([f1,f2,f3]))
        #feature = np.transpose(np.array([f0,f1,f2,f3,f7,f8]))
        # print(feature.shape)

        return feature

