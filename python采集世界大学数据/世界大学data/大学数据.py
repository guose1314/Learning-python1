import requests
import re
import xlwt

# hearders={
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"
# }
url="http://www.zuihaodaxue.cn/ARWU2019.html"
html=requests.get(url).content.decode()
daxue=re.findall(r'<tr class=".*?"><a target="_blank" href=".*?">(.*?)</a>',html)

newTable = '大学.xls'
    # 设置编码格式

def xieru_excel():
    wb = xlwt.Workbook(encoding='utf-8')
    sheet1 = wb.add_sheet(u'sheet1', cell_overwrite_ok=True)
    j = 0
    for x in daxue:
        sheet1.write(j, 1, x)
        j = j + 1
    wb.save(newTable)


