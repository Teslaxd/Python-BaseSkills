
# def func1():
#     print('abc')
#     yield 123
#     print('!!!!!!')
#     yield 100


# re = func1()
# print(re)

# # next(re) - 执行re对应的函数的函数体,将yield关键字后边的值作为结果
# print('===:', next(re))
# print('===:', next(re))
# # print('===:', next(re))
# # print('===:', next(re))

isleapyear = lambda year: (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(isleapyear(2012))
print(isleapyear(2008))
print(isleapyear(2018))
print(isleapyear(2000))


