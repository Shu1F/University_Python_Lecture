# x = int(input("Enter an unteger: "))
# ans = 0
# while ans**3 < abs(x):
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x, 'is', ans)

# 平方根を求めるためのニュートンラフソン法
# x**2 - 24 = 0 で誤差がepsilon以下になるxを求める
# count = 0
# epsilon = 0.01
# k = 24.0
# guess = k / 2.0
# while abs(guess * guess - k) >= epsilon:
#     guess = guess - (((guess**2) - k) / (2 * guess))
#     count += 1
# print("Square root of", k, "is about", guess, "Number of repetitions", count)


# # 二分法
# count = 0
# epsilon = 0.01
# k = 24.0

# low = 0.0
# high = max(1.0, k)
# guess = (high + low) / 2.0

# while abs(guess**2 - k) >= epsilon:
#     count += 1
#     if guess**2 < k:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low) / 2.0

# print("Square root of", k, "is about", guess, "Number of repetitions", count)
