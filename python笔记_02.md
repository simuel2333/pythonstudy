python 学习笔记(二)
==================
### 元组
* 定义
不可变的列表
* 定义元组
dimensions = (100,50)
dimensions[0]
dimensions[1]

### if语句
* 使用方法
cars = ['audi','benz','bmw','honda']
for car in cars:
&emsp;if car == 'audi':
&emsp;&emsp;print(car.upper())
&emsp;else:
&emsp;&emsp;print(car.title())
* 条件与
age > 10 and age < 20
* 条件或
age <= 10 or age >= 20
* 检查特定值是否包含在列表当中
'audi' in cars
'audi' not in cars
* if-elif-else结构
* if判断列表是否为空
list = []
if list

### 字典
* 字典形式
类似与json
alien = {'color': 'green', 'point': 5}
print(alien['color'])
* 删除键值对
del alien['point']
* 遍历字典
for key,value in alien.items():
&emsp;print('Key: ' + key)
&emsp;print('Value: '+ str(value))
* 遍历字典中所有的键
for key in alien.keys():
&emsp;print('Key: ' + key)
* 遍历字典中所有的值
for value in alien.values():
&emsp;print('Value: '+ str(value))
* 列表嵌套字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
&emsp;print(alien)
* 在字典中存储链表
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}
for topping in pizza['toppings']:
	print(topping)
* 在字典中使用字典
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}


