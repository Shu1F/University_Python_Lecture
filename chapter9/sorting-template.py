# -*- coding: utf-8 -*-
import time  # 時間計測
import operator  # 組込み演算子対応
import random  # randomモジュールのインポート
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
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result


def mergeSort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left, right)


# ----------------------バブルソート----------------------#
def bubbleSort(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


# ----------------------ティムソート----------------------#
def timSort(L):
    return sorted(L)


def main():
    L1 = []
    n = 1
    k = 500  # 初期の要素数
    max_k = 10000
    sel_time, merge_time, tim_time, bubble_time = [], [], [], []
    sel_ele, merge_ele, tim_ele, bubble_ele = [], [], [], []

    while k <= max_k:
        L1 = [random.randint(1, 100000) for _ in range(k)]

        # 選択ソート
        L2 = L1[:]
        start = time.time()
        selSort(L2)
        sel_time.append(time.time() - start)
        sel_ele.append(len(L2))

        # マージソート
        L3 = L1[:]
        start = time.time()
        mergeSort(L3)
        merge_time.append(time.time() - start)
        merge_ele.append(len(L3))

        # ティムソート
        L4 = L1[:]
        start = time.time()
        timSort(L4)
        tim_time.append(time.time() - start)
        tim_ele.append(len(L4))

        # バブルソート
        L5 = L1[:]
        start = time.time()
        bubbleSort(L5)
        bubble_time.append(time.time() - start)
        bubble_ele.append(len(L5))

        # 要素数を増やす
        k += 500

    # グラフ描画
    plt.figure(figsize=(10, 6))
    plt.plot(sel_ele, sel_time, label="Selection Sort", marker="o")
    plt.plot(merge_ele, merge_time, label="Merge Sort", marker="o")
    plt.plot(tim_ele, tim_time, label="Tim Sort", marker="o")
    plt.plot(bubble_ele, bubble_time, label="Bubble Sort", marker="o")

    plt.title("Comparison of Sorting Algorithms")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


main()
