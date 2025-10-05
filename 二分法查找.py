m = [6, 2, 4, 7, 1, 9, 0, 5, 3, 8, 11, 2, -2, -7]
l = len(m)  #数列元素个数
print("共有%d个数" % l)
print("排序前",m)
temp=0

i=1  #第i次循环
while i<l:  #一共l-1次循环
    j=1
    while j<=l-i:
        if m[j-1]>m[j]:
            temp=m[j]
            m[j]=m[j-1]
            m[j-1]=temp
        j=j+1
    i=i+1
print("排序后",m)

def erfenfa(nums,find,left,right):
    middle=(left+right)//2
    if nums[middle]==find:
        return middle
    if right==left+1:
        if nums[middle]!=find:
            return '没有找到'
    if nums[middle]>find:
        return erfenfa(nums,find,left,middle)
    elif nums[middle]<find:
        return erfenfa(nums,find,middle+1,right)
n=int(input('请输入查找数字：'))
print('查找数的下标为：',erfenfa(m,n,0,l))