import os
import sqlite3
os.system("color F0")
if not os.path.isdir("temp"): os.mkdir("temp")

def getField(cur,tName): #获取表字段信息
	cur.execute("PRAGMA table_info('"+tName+"')")
	aField = cur.fetchall()
	strField = ""
	aFields = [] #[字段名、类型、长度]
	for i in range(len(aField)):
		strField += aField[i][1]+","
		strLen = aField[i][2]
		if strLen.find("char")>=0:
			at1 = strLen.find("(")
			at2 = strLen.find(")")
			L = int(strLen[at1+1:].replace(")",""))
		else:
			L = 0
		aFields.append([aField[i][1],aField[i][2],L])
	if(strField): strField = strField[0:len(strField)-1]
	return aFields,strField

print("Python操作Sqlite表（建表、插入数据、获取字段信息）实例：")
con = sqlite3.connect('temp/example.db')
cur = con.cursor()
cur.execute("create table if not exists lang(lang_name, lang_age)")
cur.execute("insert into lang values (?, ?)", ("C语言", 49))
lang_list = [("Fortran语言", 64),("Python语言", 30),("Go语言", 11),]
cur.executemany("insert into lang values (?, ?)", lang_list)
con.commit()    #事务递交
cur.execute("select * from lang")
print(cur.fetchall())
print("")
aFields,strField = getField(cur,"lang")
print("获取lang表的字段名称：",strField)
print("lang表的字段详细信息：",aFields)
con.close()

os.system("echo.")  #CMD小窗口换行
os.system("echo Sqlite数据库操作演示成功。")
os.system("pause>nul")
