# def maxVal(x, y):
#     if x > y:
#         return x
#     else:
#         return y


# maxVal(3, 4)
# print(maxVal())


# isIn()
# def isIn(str1, str2):
#     if str1 in str2 or str2 in str1:
#         return True
#     else:
#         return False


# print(isIn("hello", "hello world"))
# print(isIn("goodbye", "hello world"))

# 参：https://vector-ium.com/pandas-isin/
# 　　https://note.nkmk.me/python-in-basic/


# find()


# def string(str1, str2):
#     if str1.find(str2) != -1:
#         return True
#     elif str2.find(str1) != -1:
#         return True
#     else:
#         return False


# print(string("hello", "hello world"))
# print(string("goodbye", "hello world"))

# 参：https://qiita.com/Ryo-0131/items/13115e90b5d2f19b46cc


# count()


# def string(str1, str2):
#     if str1.count(str2) != 0:
#         return True
#     elif str2.count(str1) != 0:
#         return True
#     else:
#         return False


# print(string("hello", "hello world"))
# print(string("goodbye", "hello world"))

# 参：https://note.nkmk.me/python-str-count/


# def f(x):
#     def g():
#         x = "abc"
#         print("x =", x)

#     def h():
#         z = x
#         print("z =", z)

#     x = x + 1
#     print("x =", x)
#     h()
#     g()
#     print("x =", x)
#     return g


# x = 3
# z = f(x)
# print("x =", x)
# print("z =", z)
# z()


# count = 0
# n = 5


# def fib(n):
#     global count
#     if n == 0 or n == 1:
#         return 1
#     elif n == 2:
#         global count
#         count += 1
#         return fib(n - 1) + fib(n - 2)
#     else:
#         return fib(n - 1) + fib(n - 2)


# def testFib(n):
#     for i in range(n + 1):
#         print("fib of", i, "=", fib(i))


# # n = 5の計算
# print(fib(n))
# print("呼び出し回数：", count)
