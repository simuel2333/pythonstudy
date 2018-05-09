python 学习笔记(三)
================
###用户输入与while循环
* 用户输入
input()
input("Please input something: ")
* 将字符串数字转换成整数
int()
* while 循环
n = 0
while n < 6:
&emsp;print(n)
&emsp;n += 1
* 使用break推出while循环
* 在循环中使用continue

###在while循环中处理列表和字典
* 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
&emsp;pets.remove("cat")

###函数
* 定义函数
def greet_user():
&emsp;print("Hello!")
* 传递参数
def greet_user(name):
&emsp;print("Hello," + name + "!")
greet_user('Tom')
* 实参和形参
形参：函数完成其工作所需的一项信息，name
实参：实参是调用函数时传递给函数的信息，'Tom'
* 位置实参
def f(type,name):
...
调用时传递的实参需和形参顺序一致
* 关键字实参
f(type = 'a', name = 'bob')
f(name = 'candy', type = 'b')
* 函数默认值
def f(type, name="cheng"):
...
* 函数返回值
return ...
* 禁止函数修改列表
function_name(list_name[:])
传递一个列表的副本，但没有充足的理由不要使用列表的副本
* 传递任意数量的实参
def make_pizza(\*toppings):
...
\*topppings将接收的实参转换为一个形参元组。
* 使用任意数量的关键字参数
def build_profile(first_name, last_name, \*\*user_info):
...
\*\*user_info让python创建一个空字典uer_info,并将所有收到的名称值都封装到这个字典中
