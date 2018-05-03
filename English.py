import re

filename = 'worryfa.txt'

# 文件操作
with open(filename) as file_object:
    lines = file_object.readlines()

# 读取文件
sum =[]
p = re.compile('[a-zA-Z]')
for line in lines:
    a = []
    for dangci in line:
        if (p.match(dangci)):
            a.append(dangci)
        else:
            b = ''.join(a) # 将列表转化为字符串
            if len(b) >= 2:
                sum.append(b.lower())
                a = []


# 数据清洗
k =[]
for i in range(0, len(sum)):
    if(sum[i] == ''):
        k.append(i)

i = len(k)-1 # 删除空格
while(i > 0):
    sum.pop(int(k[i]))
    i -= 1

#计算出词频
values = []
num = 0
cunter = 0
for i in sum:
    a = i
    for j in sum:
        if(a == j):
            num +=1
    values.append(num)
    num = 0
    cunter += 1
del num, cunter
# ----------------------------
print(len(values), len(sum)) #
# ----------------------------

# 两个列表合并为字典
ci = {}
print(len(sum), len(values), '\n', '-----------------------')
for i in range(0, int(len(sum))):
    ci[sum[i]] = values[i] # 在这里就可以自动删除重复健值

b = sorted(ci.items(), key = lambda item:item[1], reverse=True)


# 读入文件
with open('ciping.txt','w') as file_object:
    for i in b:
        for k in i:
            tep = str(k)
            file_object.write(tep)
            file_object.write(' ')
        file_object.write('\n')
