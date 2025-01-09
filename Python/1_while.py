# numXs = int(input('How many times should I print the letter X? '))
# toPrint = ''
# # numXs回だけtoPrintにXを連結する
# print(toPrint)

# ↑をwhile文に書き換える

# numXs = int(input("How many times should I print the letter X? "))
# toPrint = ""
# # numXs回だけtoPrintにXを連結する
# while numXs != 0:
#     toPrint = toPrint + "X"
#     numXs -= 1
# print(toPrint)


# ユーザーに10個の正の整数の入力を促したうえ。その中で最も大きな奇数の値を表示するプログラム

x = []
n = 10
max = 0

# 入力を繰り返してリストを作成する
while n > 0:
    x.append(int(input("enter number " + str(n) + ": ")))
    n -= 1

# 確認用にプリントしてみる
# print(x)

x = []
n = 10
max = 0

# 入力を繰り返してリストを作成する
while n > 0:
    x.append(int(input("enter number " + str(n) + ": ")))
    n -= 1

# 確認用にプリントしてみる
# print(x)

# x = []
# n = 10
# max = 0

# # 入力を繰り返してリストを作成する
# while n > 0:
#     x.append(int(input('enter number ' + str(n) + ': ')))
#     n -= 1

# # 確認用にプリントしてみる
# #print(x)

# n = 0
# while n < 10:
#     if x[n] % 2 == 0:  # 偶数だったら0にしてしまう
#         x[n] = 0
#     else:
#         if max < x[n]:  # 奇数で、maxより大きい場合はmaxを置き換える
#             max = x[n]
#     n += 1

# if max == 0:  # 偶数しか無い場合
#     print("No Odd number")
# else:
#     print("Max odd number is", max)
