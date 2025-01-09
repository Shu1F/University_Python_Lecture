# 某国のマクドナルドでは、チキンマックナゲットは3種類のパッケージがある。
# 6個入り、9個入り、20個入り の3種類である。これを組み合わせて買うことで、ほぼ
# あらゆる数の「合計数」を買うことができる、という点でよく出来た組み合わせである。こ
# れを以下の手順で確認してみよう。


# 問1.合計で、50, 51, 52, 53, 54, 55 個のナゲットを買うことができることを示せ。 手計
# 算でもプログラムでも良い。それぞれの場合の、6個、9個、20個パッケージの必要数を
# (a, b, c) の形で解答すること。

# def find_combinations(target):
#     for a in range(target // 6 + 1):
#         for b in range(target // 9 + 1):
#             for c in range(target // 20 + 1):
#                 if 6 * a + 9 * b + 20 * c == target:
#                     return a, b, c
#     return None

# # 50～55個のナゲットについて確認
# for n in range(50, 56):
#     result = find_combinations(n)
#     if result:
#         print(f"{n}個: {result}")
#     else:
#         print(f"{n}個: 買う組み合わせが見つかりませんでした")

# 問2.上記の結果を用いて、合計で 56, 57, ..., 65 個のナゲットを買うことができる組み合
# わせが存在することを示せ。

# # 56～65個のナゲットについて確認
# for n in range(56, 66):
#     result = find_combinations(n)
#     if result:
#         print(f"{n}個: {result}")
#     else:
#         print(f"{n}個: 買う組み合わせが見つかりませんでした")

# 問3.以上のことを参考に考えると、以下の定理が導かれる。
# 「もし、x, x+1, x+2, ... , x+5 個を買う組み合わせが存在するなら、x 以上のすべての数を
# 買う組み合わせが存在する」 なぜこれが成立するか説明せよ。(厳密な証明でなくて良い)


# 問4.上記の定理および設問2の結果を合わせて考えると、n 個以上の数については、どん
# な数であってもぴったり買う組み合わせが存在する(n は自分で考えること)。すると、ある
# 3種類のパッケージ数の組、ここでは(6, 9, 20) が与えられたときこれに対して、「ぴった
# りの数で買うことのできない最大の数」が決まるはずである。これを求めるプログラムを書
# け。
# Hint: n 個が買えるかどうかの判定をする関数: kaerukana(n) を再帰的に定義することで綺
# 麗に書ける。ベースケースをどうするかをよく考えること。

# def kaerukana(n):
#     if n < 0:
#         return False
#     if n == 0:
#         return True
#     return kaerukana(n - 6) or kaerukana(n - 9) or kaerukana(n - 20)

# def find_largest_unreachable():
#     n = 1
#     while True:
#         if not kaerukana(n):
#             max_unreachable = n
#         else:
#             break
#         n += 1
#     return max_unreachable

# print(f"最大の買えない数: {find_largest_unreachable()}")

# 問5.上の設問は、パッケージの組み合わせが 6, 9, 20 個入りの場合であった。これを一般
# 化しよう。すなわちそれぞれのパッケージあたり個数が、x, y, z のときに、最大の買えない
# 数 n を求めるプログラムを書け。これも再帰を用いる。

# def kaerukana_general(n, x, y, z):
#     if n < 0:
#         return False
#     if n == 0:
#         return True
#     return kaerukana_general(n - x, x, y, z) or kaerukana_general(n - y, x, y, z) or kaerukana_general(n - z, x, y, z)

# def find_largest_unreachable_general(x, y, z):
#     n = 1
#     while True:
#         if not kaerukana_general(n, x, y, z):
#             max_unreachable = n
#         else:
#             break
#         n += 1
#     return max_unreachable

# # 例: 6, 9, 20
# print(f"(6, 9, 20) の最大の買えない数: {find_largest_unreachable_general(6, 9, 20)}")

# 問 6. 上記の問 4, 問 5 で再帰を用いるのはプログラマにとっては読みやすいが、コンピュ
# ータにとっては計算効率が悪い。dictionary を用いて効率化せよ。どの程度効率化されたか、
# 定量的に評価し、グラフで示し、考察せよ。

# def kaerukana_memoized(n, x, y, z, memo):
#     if n < 0:
#         return False
#     if n == 0:
#         return True
#     if n in memo:
#         return memo[n]
#     memo[n] = (kaerukana_memoized(n - x, x, y, z, memo) or
#                kaerukana_memoized(n - y, x, y, z, memo) or
#                kaerukana_memoized(n - z, x, y, z, memo))
#     return memo[n]

# def find_largest_unreachable_memoized(x, y, z):
#     memo = {}
#     n = 1
#     while True:
#         if not kaerukana_memoized(n, x, y, z, memo):
#             max_unreachable = n
#         else:
#             break
#         n += 1
#     return max_unreachable

# # 例: 6, 9, 20
# print(f"(6, 9, 20) の最大の買えない数 (効率化): {find_largest_unreachable_memoized(6, 9, 20)}")
