#pip install baidu-aip
from aip import AipOcr


appId = "14398296"
apiKey = "QjvbGRIjvSax45vRSAMQ0oBC"
secretKey = "zaX8Kwzsf8unAEMTGGP1AdsKuHGGHGKE"
client = AipOcr(appId, apiKey, secretKey)

#读取图片
def getFileContent(filePath):
    with open(filePath, "rb") as f:
        return f.read()
#测试文件 也可以写路径
image = getFileContent("123.gif")
#调用通用的文字识别，图片参数为本地图片
result = client.basicGeneral(image)
#定义一个参数变量
options = {
    #定义图像的方向
    "detec_direction": "true",
    #识别的语言类型 默认中英文
    "language_type": "CHN_ENG"
}
#调用通用文字识别的接口
results = client.basicGeneral(image,options)
print(results)

# for item in results["words_result"]:
#     print(item["words"])
