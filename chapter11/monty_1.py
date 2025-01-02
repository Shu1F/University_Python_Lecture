# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
def Monty(max, step):   #最大数、ステップ数を受け取る
	ncWinp = []       # no-changeで勝った回数記録
	cWinp = []        # change で勝った回数記録
	n = range(10,max,step)   #n回プレイする。nは10からmaxまで
	for numPlay in n:
		ncWin = 0
		cWin = 0
		for i in range(0,numPlay):
			if NoChange() == "new_car":#no-change 当たったら
				ncWin += 1              #1増やす
							#Changeの場合も同様にあたったらカウンタを１増やす

		ncWinp.append(ncWin/numPlay)  #勝率をリストに追加、Changeの場合も同様に

	plt.figure()                            #以下はグラフプロット。必要に応じて調整する。
	plt.plot(n,cWinp,"b")
	plt.plot(n,ncWinp,"r")
	plt.title("Winning Ratio")
	plt.xlabel("Number of Trial"),plt.ylabel("Winning Ratio")
	plt.ylim(0.0,1.0)
	plt.legend(("Change","No-Change"),loc="best")
	plt.show()
    
def NoChange():
	CARis = random.choice(["A","B","C"])  #正解をランダムに選んでおく
	PlayerChoice = random.choice(["A","B","C"]) #選択したのはこれ
	if PlayerChoice == CARis:      #正解＝選択　一致してたら
		return "new_car"
	else:
		return "goat"
    
def DoChange():
	CARis = random.choice(["A","B","C"])     #正解をランダムに選んでおく
	PlayerFirstChoice = random.choice(["A","B","C"])  #選択したのはこれ

#ここまではNoChangeと同じ　以下、Changeの場合を記述しよう

#　MontyChoice のドアを決定して開ける

#　Player2ndChoice = door  #これを変更後の選択とする
#結果の返し方もNoChangeの場合と同じにしておく

	if Player2ndChoice == CARis:
		return "new_car"
	else:
		return "goat"
	
Monty(N, m)   #最大 N 回まで。m回刻みで実行。N, mは適宜変更してみること。

