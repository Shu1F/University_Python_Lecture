# import numpy as np
# import matplotlib.pyplot as plt

# epsilon = [
#     0.1,
#     0.01,
#     0.001,
#     0.0001,
#     0.00001,
#     0.000001,
#     0.0000001,
#     0.00000001,
#     0.000000001,
# ]

# # bisection method
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
# # グラフをプロット
# plt.semilogx(epsilon, numGuess_newton, "x-", label="Newton-Raphson")
# plt.semilogx(epsilon, numGuess_bisec, "+-", label="Bisection")
# plt.legend()
# plt.show()
