# -*- coding: utf-8 -*-
# 必要最小限の骨組みだけで、それぞれのソートアルゴリズムは記述されていません。
# 1). 各アルゴリズムを実装すること。
# 2). グラフは、それぞれ単独で適当なスケールで表示されています。
#     これだけでは異なるアルゴリズムの比較が困難です。同じスケールで表示する、
#     同じグラフに重ねて表示するなど、適宜考えて見やすい表示を行うこと。
#     やり方は、"matplotlib  pyplot" などを調べること。あるいはテキスト
#     11章のPyLab、その他のツールを用いるのもOKです。

import time  # 時間計測
import operator  # 組込み演算子対応
import random  # randomモジュールのインポート
import matplotlib.gridspec as gridspec  # グラフを分ける
import matplotlib.pyplot as plt  # plotするため


# ----------------------選択ソート----------------------#
def selSort(L):
    for i in range(len(L)):
        min_idx = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_idx]:
                min_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]
    return L


# ----------------------マージソート----------------------#
def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergeSort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    mid = len(L) // 2
    left = mergeSort(L[:mid], compare)
    right = mergeSort(L[mid:], compare)
    return merge(left, right, compare)


# ----------------------ティムソート----------------------#
def timSort(L):
    return sorted(L)


# ----------------------バブルソート----------------------#
def bubbleSort(L):
    for i in range(len(L)):
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


def main():
    sel_time = []
    sel_ele = []
    merge_time = []
    merge_ele = []
    tim_time = []
    tim_ele = []
    bubble_time = []
    bubble_ele = []

    for k in range(500, 5001, 500):  # 500から5000まで500刻み
        L1 = [random.randint(1, 100000) for _ in range(k)]
        L2 = L1[:]
        L3 = L1[:]
        L4 = L1[:]

        start = time.process_time()
        selSort(L1)
        sel_time.append(time.process_time() - start)
        sel_ele.append(len(L1))

        start = time.process_time()
        mergeSort(L2)
        merge_time.append(time.process_time() - start)
        merge_ele.append(len(L2))

        start = time.process_time()
        timSort(L3)
        tim_time.append(time.process_time() - start)
        tim_ele.append(len(L3))

        start = time.process_time()
        bubbleSort(L4)
        bubble_time.append(time.process_time() - start)
        bubble_ele.append(len(L4))

    # ---------------------------------グラフの描画例-----------------------------------#
    plt.figure(figsize=(10, 6))
    plt.plot(sel_ele, sel_time, label="Selection Sort", marker="o")
    plt.plot(merge_ele, merge_time, label="Merge Sort", marker="o")
    plt.plot(tim_ele, tim_time, label="Timsort (Python Built-in)", marker="o")
    plt.plot(bubble_ele, bubble_time, label="Bubble Sort", marker="o")

    plt.title("Comparison of Sorting Algorithms")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.yscale("log")  # y軸を対数スケールに設定
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


main()
