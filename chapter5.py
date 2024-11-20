# 問１
# def nugget(pieces, a=0, b=0, c=0):
#     if pieces == 0:
#         return [(a, b, c)]

#     if pieces < 0:
#         return []

#     nuggetCombination = []

#     nuggetCombination += nugget(pieces - 6, a + 1, b, c)
#     nuggetCombination += nugget(pieces - 9, a, b + 1, c)
#     nuggetCombination += nugget(pieces - 20, a, b, c + 1)

#     return nuggetCombination


# for n in range(50, 56):
#     print(f"{n}個")
#     result = nugget(n)
#     if result:
#         for combination in result:
#             print(
#                 f"６個入り：{combination[0]}個, ９個入り：{combination[1]}個, ２０個入り：{combination[2]}個"
#             )

#     else:
#         print("組み合わせなし")


# 問１
# def nugget(pieces, a=0, b=0, c=0):
#     if pieces == 0:
#         return [(a, b, c)]
#     if pieces < 0:
#         return []

#     nuggetCombination = []
#     nuggetCombination += nugget(pieces - 6, a + 1, b, c)
#     nuggetCombination += nugget(pieces - 9, a, b + 1, c)
#     nuggetCombination += nugget(pieces - 20, a, b, c + 1)

#     return list(set(nuggetCombination))


# for n in range(50, 56):
#     print(f"{n}個のナゲット:")
#     result = nugget(n)
#     if result:
#         for combination in result:
#             print(
#                 f"６個入り：{combination[0]}個, ９個入り：{combination[1]}個, ２０個入り：{combination[2]}個"
#             )
#     else:
#         print("組み合わせなし")


# 問１<辞書型>
# def nugget(pieces, a=0, b=0, c=0):
#     if pieces == 0:
#         return [{"6個入り": a, "9個入り": b, "20個入り": c}]
#     if pieces < 0:
#         return []

#     nuggetCombination = []
#     nuggetCombination += nugget(pieces - 6, a + 1, b, c)
#     nuggetCombination += nugget(pieces - 9, a, b + 1, c)
#     nuggetCombination += nugget(pieces - 20, a, b, c + 1)

#     return [dict(t) for t in {tuple(d.items()) for d in nuggetCombination}]


# for n in range(50, 56):
#     print(f"{n}個のナゲット:")
#     result = nugget(n)
#     if result:
#         for combination in result:
#             print(
#                 f"６個入り：{combination['6個入り']}個, ９個入り：{combination['9個入り']}個, ２０個入り：{combination['20個入り']}個"
#             )
#     else:
#         print("組み合わせなし")


# # 問２
# ＜再帰型＞
# def nugget_recursive(pieces, a=0, b=0, c=0):
#     if pieces == 0:
#         return [(a, b, c)]
#     if pieces < 0:
#         return []

#     nuggetCombination = []
#     nuggetCombination += nugget_recursive(pieces - 6, a + 1, b, c)
#     nuggetCombination += nugget_recursive(pieces - 9, a, b + 1, c)
#     nuggetCombination += nugget_recursive(pieces - 20, a, b, c + 1)

#     return list(set(nuggetCombination))


# for n in range(56, 66):
#     print(f"{n}個のナゲット:")
#     result = nugget_recursive(n)
#     if result:
#         for combination in result:
#             print(
#                 f"６個入り：{combination[0]}個, ９個入り：{combination[1]}個, ２０個入り：{combination[2]}個"
#             )
#     else:
#         print("組み合わせなし")

# ＜辞書型＞
# def nugget_dict(pieces, a=0, b=0, c=0):
#     if pieces == 0:
#         return [{"6個入り": a, "9個入り": b, "20個入り": c}]
#     if pieces < 0:
#         return []

#     nuggetCombination = []
#     nuggetCombination += nugget_dict(pieces - 6, a + 1, b, c)
#     nuggetCombination += nugget_dict(pieces - 9, a, b + 1, c)
#     nuggetCombination += nugget_dict(pieces - 20, a, b, c + 1)

#     return [dict(t) for t in {tuple(d.items()) for d in nuggetCombination}]


# for n in range(56, 66):
#     print(f"{n}個のナゲット:")
#     result = nugget_dict(n)
#     if result:
#         for combination in result:
#             print(f"６個入り：{combination['6個入り']}個, ９個入り：{combination['9個入り']}個, ２０個入り：{combination['20個入り']}個")
#     else:
#         print("組み合わせなし")

# 問３


# 問４
# def kaerukana(n):
#     if n == 0:
#         return True
#     if n < 0:
#         return False
#     # 再帰的に6、9、20パックを減らしていき、買えるかを判定
#     return kaerukana(n - 6) or kaerukana(n - 9) or kaerukana(n - 20)


# def max_unreachable():
#     n = 1
#     last_unreachable = 0  # 最後に買えなかった数
#     consecutive_count = 0  # 連続して買える数のカウント

#     while consecutive_count < 6:  # 連続して6個の数が買えるまでループ
#         if kaerukana(n):
#             consecutive_count += 1
#         else:
#             last_unreachable = n
#             consecutive_count = 0  # 買えない数が見つかったらリセット
#         n += 1

#     return last_unreachable


# # 実行
# print("ぴったり買うことのできない最大の数:", max_unreachable())

# 問５


# def kaerukana(n, x, y, z):
#     if n == 0:
#         return True
#     if n < 0:
#         return False
#     # 再帰的にx、y、zパックを減らしていき、買えるかを判定
#     return (
#         kaerukana(n - x, x, y, z)
#         or kaerukana(n - y, x, y, z)
#         or kaerukana(n - z, x, y, z)
#     )


# def max_unreachable(x, y, z):
#     n = 1
#     last_unreachable = 0  # 最後に買えなかった数
#     consecutive_count = 0  # 連続して買える数のカウント

#     while consecutive_count < 6:  # 連続して6個の数が買えるまでループ
#         if kaerukana(n, x, y, z):
#             consecutive_count += 1
#         else:
#             last_unreachable = n
#             consecutive_count = 0  # 買えない数が見つかったらリセット
#         n += 1

#     return last_unreachable


# # 実行例
# x, y, z = 6, 9, 20  # 任意のパッケージのサイズ
# print(
#     f"{x}, {y}, {z}のパッケージのとき、ぴったり買うことのできない最大の数:",
#     max_unreachable(x, y, z),
# )


# メモ化を使用しない関数
def kaerukana_no_memo(n):
    if n == 0:
        return True, 1  # 呼び出し回数1を返す
    if n < 0:
        return False, 1  # 呼び出し回数1を返す

    result1, count1 = kaerukana_no_memo(n - 6)
    result2, count2 = kaerukana_no_memo(n - 9)
    result3, count3 = kaerukana_no_memo(n - 20)

    # 任意の結果がTrueならTrueとし、呼び出し回数の合計を返す
    return (result1 or result2 or result3), count1 + count2 + count3 + 1


# メモ化を使用した関数
def kaerukana_with_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n], 1  # 呼び出し回数1を返す
    if n == 0:
        return True, 1
    if n < 0:
        return False, 1

    result1, count1 = kaerukana_with_memo(n - 6, memo)
    result2, count2 = kaerukana_with_memo(n - 9, memo)
    result3, count3 = kaerukana_with_memo(n - 20, memo)

    # 計算結果と呼び出し回数を返す
    result = result1 or result2 or result3
    memo[n] = result
    return result, count1 + count2 + count3 + 1


# 各nについて計算回数を測定
data = []
for n in range(20, 50):  # nの範囲を変更できます
    # メモ化なしの計算
    _, no_memo_count = kaerukana_no_memo(n)

    # メモ化ありの計算
    _, with_memo_count = kaerukana_with_memo(n)

    # 結果をリストに追加
    data.append((n, no_memo_count, with_memo_count))

# 結果をCSVファイルに保存
import csv

with open("nugget_combinations_counts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["n", "no_memo_count", "with_memo_count"])
    writer.writerows(data)

print("CSVファイルに保存完了")
