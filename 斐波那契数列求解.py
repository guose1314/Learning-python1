def fab(n):
    if n<1:
        print('输出错误')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

number=int(input("请问想知道多少个月后的兔子数量："))
result=fab(number)
print("%d个月后兔子的个数是：%d" % (number,result))
