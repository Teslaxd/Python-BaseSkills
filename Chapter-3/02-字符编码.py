# author： Mark

"""
1.什么是字符串
序列，有序，不可变的。
用单引号或者双引号括起来的任意字符集。

2.字符串中的字符
a.普通字符: '23'，'ashNHJ','-=+!$@% #^&><?', '上的惊世毒妃', '🌲🐶🌺'
b.转义字符：\n, \t, \', \", \\
阻止转义：r/R
"""

# 1.字符编码
"""
python中的字符采用的是Unicode编码

a.什么是编码
就是数字和字符的一一对应的，其中字符对应数字就是字符的编码
a - 97
b - 98
余 - 20313

b.编码方式
ASCII码表：针对数字字符、字母字符、一些英文中常用的符号进行编码
          采用一个字节对字符进行编码（128个字符）
Unicode码：Unicode码包含了ASCII码表，同时能够对世界上所有语言对应符号进行编码
          采用两个字节对字符进行编码,能编码65536个字符
          中文：4E00 ~ 9FA5
          
c.两个函数
chr(编码值) - 将字符编码转换成字符
ord(字符) - 获取字符对应的编码值

"""
print(chr(0x4E01))
liu = ord('刘')
ting = ord('婷')
print(hex(yu), hex(ting))

# d.可以将字符编码放到字符串中便是一个字符: \u + 4位的16进制编码值
str1 = 'abc\u4f59123\u1234'
print(str1)