python 学习笔记(一)
================
### 字符串相关
* 字符串函数
title()
upper()
lower()
* 删除空白
rstrip()
lstrip()
strip()
* 显示转换
str()：在拼接字符串时如果有数字要拼接，python不会隐示转换需要使用str()函数。
* 注释
`#`
* python之禅
import this

### 列表相关
* 列表(数组)
fruits = ['apple','orange','banana']：数组中的元素既可以是字符串也可以是数字。
* 数组追加元素
fruits.append('pear')
* 在数组中插入元素
fruits.insert(0,'wartermelon')
* 在数组中删除元素
del fruits[1]：删除第二个元素
* pop()删除列表中的元素
fruits.pop()：相当于出栈会返回出栈的元素
fruits.pop(0):弹出第一个位置的元素
* 根据值删除元素remove()
fruits.remove('apple')
* 列表永久性排序
sort()
sort(reverse=True)
* 列表临时性排序
sorted()
sorted(reverse=True)
* 列表倒序
reverse()
* 列表长度
len(fruits)
* 列表负数序号
fruits[-1]：倒数第一个列表元素，fruits[-2]：倒数第二个列表元素......

### 操作列表
* 遍历整个列表
for fruit in fruist:
&emsp;print(fruit)
* for循环中的每项任务必须缩进。
* 不必要的缩进要避免
* 循环后不必要的缩进要避免
* 创建数值列表
range(1,5)
list(range(1,5)):[1,2,3,4]
list(range(1,10,2)):[1,3,4,5,7,9]第三个参数指定步长
* 对数字列表进行简单的统计计算
min(nums)
max(nums)
sum(nums)
* 列表解析
cubes = [value**3 for value in range(1,11)]:生成包含前十个数的立方
* 列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
players[1:4]
players[:4]
players[3:]
players[-3:]
* 遍历切片
for player in players[1:4]:
&emsp;print(player.title())
* 列表复制
players_copy = players[:]
