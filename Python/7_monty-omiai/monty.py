# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt


def Monty(max, step):  # 最大数、ステップ数を受け取る
    ncWinp = []  # no-changeで勝った回数記録
    cWinp = []  # changeで勝った回数記録
    n = range(10, max, step)  # n回プレイする。nは10からmaxまで
    for numPlay in n:
        ncWin = 0
        cWin = 0
        for i in range(0, numPlay):
            if NoChange() == "new_car":  # no-change 当たったら
                ncWin += 1  # 1増やす
            if DoChange() == "new_car":  # change 当たったら
                cWin += 1  # 1増やす

        ncWinp.append(ncWin / numPlay)  # 勝率をリストに追加
        cWinp.append(cWin / numPlay)  # Changeの場合も同様に

    plt.figure()  # 以下はグラフプロット。必要に応じて調整する。
    plt.plot(n, cWinp, "b")
    plt.plot(n, ncWinp, "r")
    plt.title("Winning Ratio")
    plt.xlabel("Number of Trials")
    plt.ylabel("Winning Ratio")
    plt.ylim(0.0, 1.0)
    plt.legend(("Change", "No-Change"), loc="best")
    plt.show()


def NoChange():
    CARis = random.choice(["A", "B", "C"])  # 正解をランダムに選んでおく
    PlayerChoice = random.choice(["A", "B", "C"])  # 選択したのはこれ
    if PlayerChoice == CARis:  # 正解＝選択 一致してたら
        return "new_car"
    else:
        return "goat"


def DoChange():
    CARis = random.choice(["A", "B", "C"])  # 正解をランダムに選んでおく
    PlayerFirstChoice = random.choice(["A", "B", "C"])  # 初回選択

    # Montyがヤギのいるドアを選んで開ける
    doors = ["A", "B", "C"]
    doors.remove(PlayerFirstChoice)
    if CARis in doors:
        doors.remove(CARis)  # ヤギのドアを残す
    MontyChoice = random.choice(doors)

    # プレイヤーが変更する
    remaining_doors = ["A", "B", "C"]
    remaining_doors.remove(PlayerFirstChoice)
    remaining_doors.remove(MontyChoice)
    Player2ndChoice = remaining_doors[0]  # 変更後の選択

    if Player2ndChoice == CARis:
        return "new_car"
    else:
        return "goat"


# シミュレーションの実行
N = 1000  # 最大試行回数
m = 100  # ステップ
Monty(N, m)
