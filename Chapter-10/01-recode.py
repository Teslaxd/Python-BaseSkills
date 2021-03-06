# author: Mark

"""
1.容器类数据类型
a.列表:可变，有序
b.元祖:x, y = 12, 100;  x, *num = 12, 33, 45, 23; (10,)。 不可变， 有序
c.字典:可变，无序
d.集合:可变，无序； 元素唯一； 支持数学的集合运算



2.函数
a.函数的声明
def 函数名(参数列表):
    函数体
    
b.函数的调用
回到函数声明的位置
传参(使用实参给形参赋值)
执行函数体
确定返回值
回到函数调用的位置

c.参数
位置参数和关键字参数

参数的默认值
不定长参数: 不带*要放在带*的前面， 带一个*要放在带两个*的前面
参数和返回值类型说明:   

d.返回值
怎么确定一个函数的返回?
函数调用表达式 - 就是函数的返回值

调用函数：1）会执行函数体   2）获取返回值

c.匿名函数
lambda 参数列表: 返回值  

d.作用域
全局变量
局部变量
global: 只能在函数中使用, 声明一个全局变量
nonlocal:只能在函数中使用,在子函数中声明一个父函数的局部变量

e.函数作为变量
声明函数的时候就是在声明一个变量，函数名就是变量名
"""
a = 10
func2 = lambda x: x*2


def func1(name: str, n, *num, **num2) -> int:
    print(name, n, num, num2)
    return 100


func1('and', 23, 89, 890)


for x in range(10):
    print(x)


print(x)


def func3():

    print(x)
    return 100


a = func3    # a最后是一个函数
b = func3()  # b最后是数字100


#  func4是全局变量
def func4():
    print('func4')

    # func5是局部变量
    def func5():
        print('func5')

    func5()


func4()
# func5()