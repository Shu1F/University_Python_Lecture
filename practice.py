import matplotlib.pyplot as plt

# numXs = int(input("How many times should I print the letter X?"))
# toPrint = ""

# while numXs != 0:
#     toPrint = toPrint + "X"
#     numXs = numXs - 1

# print(toPrint)

# number = input("Please type 10 integer").split()

# number = [int(num) for num in number]

# odd_Numbers = []

# for num in number:
#     if num % 2 == 1:
#         odd_Numbers.append(num)

# if odd_Numbers:
#     max_number = max(odd_Numbers)
#     print(f"The largest odd number is: {max_number}")
# else:
#     print("There are no odd numbers in the input.")


# x = int(input("Enter an integer: "))
# ans = 0


# while ans**3 < abs(x):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, "is not a perfect cube")
# else:
#     if x < 0:
#         ans = -ans
#     print("Cube root of", x, "is", ans)

# ユーザーに正の整数を入力させる
# number = int(input("Please enter a positive integer: "))

# # 条件に合う root と pwr を探す
# found = False  # 条件に合うペアが見つかったかどうかを示すフラグ

# for root in range(1, number + 1):  # root の範囲は 1 以上
#     for pwr in range(1, 6):  # pwr の範囲は 1 以上 5 以下
#         if root**pwr == number:
#             print(f"root = {root}, pwr = {pwr}")
#             found = True
#             break  # 見つけたら内側のループを終了
#     if found:
#         break  # 外側のループも終了

# # 条件に合うペアが見つからない場合のメッセージ
# if not found:
#     print("No such pair of root and pwr found.")


# # bisection method
# epsilon = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001]
# numGuess_bisec = []

# for ep in epsilon:
#     x = 100000
#     numGuesses = 0
#     low = 0.0
#     high = max(1.0, x)
#     ans = (high + low) / 2.0

#     while abs(ans**2 - x) >= ep:
#         numGuesses += 1
#         if ans**2 < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low) / 2.0

#     numGuess_bisec.append(numGuesses)
#     print("epsilon =", ep)
#     print("numGuesses =", numGuesses)

# print(numGuess_bisec)
# # Newton-Raphson method
# numGuess_newton = []


# for ep in epsilon:
#     k = 100000.0
#     guess = k / 2.0
#     numGuesses = 0

#     while abs(guess * guess - k) >= ep:
#         guess = guess - (((guess**2) - k) / (2 * guess))
#         numGuesses += 1

#     numGuess_newton.append(numGuesses)
#     print("epsilon =", ep)
#     print("numGuesses =", numGuesses)

# print(numGuess_newton)


# plt.semilogx(epsilon, numGuess_newton, "x-", label="Newton-Raphson")
# plt.semilogx(epsilon, numGuess_bisec, "+-", label="Bisection")
# plt.legend()
# plt.show()


# def isIn(str1, str2):
#     if str1 in str2 or str2 in str1:
#         return True
#     else:
#         return False


# 使用例
# print(isIn("sleep", "eep"))  # True
# print(isIn("hello", "world"))  # False


# def printName(firstName, lastName, reverse):
#     if reverse:
#         print(lastName + ", " + firstName)
#     else:
#         print(firstName, lastName)


# printName("阿邊", "拓真", False)
# printName("鈴木", "陽希", reverse=False)
# printName("菊池", lastName="翔吾", reverse=False)
# printName(lastName="秀一", firstName="藤池", reverse=False)


def f(x):
    y = 1
    x = x + y
    print("x =", x)
    return x


x = 3
y = 2
z = f(x)
print("z =", z)
print("x =", x)
print("y =", y)
