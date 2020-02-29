# author： Mark

"""
1.格式字符串
指的是字符串中通过格式占位符来表示字符串中变化，然后后面再通过其他的值来给占位符赋值
语法：
含有格式占位符的字符串 % (占位符对应的值)

说明：格式占位符 - 有固定的写法;可以有多个
     % - 固定写法
     () - 里面的值的个数和值的类型要和前面的格式占位符一一对应

2.常见格式占位符
%d - 整数
%s - 字符串
%.nf - 小数(保留小数点后n位小数)
%c - 字符 (可以将字符编码转换成字符)
"""

name = input('名字:')
message = '%s你好，吃饭了吗？' % (name)
print(message)

message = '%s,今年%d岁，体重:%.2fkg 血型是：%c' % (name, 18+2, 65, 97)
print(message)

message = name + ',今年'+ str(18+2)+'岁，体重:'+ str(65)+'kg 血型是：'+chr(97)
print(message)