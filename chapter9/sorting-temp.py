# -*- coding: utf-8 -*-
# 必要最小限の骨組みだけで、それぞれのソートアルゴリズムは記述されていません。
# 1). 各アルゴリズムを実装すること。
# 2). グラフは、それぞれ単独で適当なスケールで表示されています。
#     これだけでは異なるアルゴリズムの比較が困難です。同じスケールで表示する、
#     同じグラフに重ねて表示するなど、適宜考えて見やすい表示を行うこと。
#     やり方は、"matplotlib  pyplot" などを調べること。あるいはテキスト
#     11章のPyLab、その他のツールを用いるのもOKです。

import time                                         #時間計測
import operator                                     #組込み演算子対応
import random                                       #randomモジュールのインポート
import matplotlib.gridspec as gridspec              #グラフを分ける
import matplotlib.pyplot as plt                     #plotするため

#----------------------選択ソート----------------------#
def selSort(L):
#
#
    return L

#----------------------マージソート----------------------#
def merge(left,right,compare):
    result=[]
#
    return result
		

def mergeSort(L,compare=operator.lt):
#
#        return merge(left,right,compare)
    return(L)                                       #これはダミーです
#----------------------ティムソート----------------------#
def timSort(L):
    return sorted(L)
#----------------------バブルソート----------------------#
def bubbleSort(L):	
#
    return L

def main():
    L1=[]
    n=1
    k=0
    sel_time=[]                                     #sel縦軸
    sel_ele=[]                                      #sel横軸
    merge_time=[]                                   #merge縦軸
    merge_ele=[]                                    #merge横軸
    tim_time=[]                                     #tim縦軸
    tim_ele=[]                                      #tim横軸
    bubble_time=[]                                  #bubble縦軸
    bubble_ele=[]                                   #bubble横軸


    for plot in range(0,5):           #plot数 逐次増やすmax20程度
        while n<k:                                  #k個乱数生成
            L1.append(random.randint(1,100000))     #乱数の範囲
            n+=1
        L2=L1[:]                                    #乱数コピー
        L3=L1[:]                                    #乱数コピー
        L4=L1[:]                                    #乱数コピー

        start=time.clock()                          #計測開始
        sel_ans=selSort(L1)
        sel_time.append(time.clock()-start)         #計測終了
        sel_ele.append(len(L1))
        
        start=time.clock()                          #計測開始
        merge_ans=mergeSort(L2)
        merge_time.append(time.clock()-start)       #計測終了
        merge_ele.append(len(L2))
        
        start=time.clock()                          #計測開始
        tim_ans=timSort(L3)
        tim_time.append(time.clock()-start)         #計測終了
        tim_ele.append(len(L3))
        
        start=time.clock()                          #計測開始
        bubble_ans=bubbleSort(L4)
        bubble_time.append(time.clock()-start)      #計測終了
        bubble_ele.append(len(L4))
        
        n=1                                         #乱数の個数初期化
        k+=500                                     #要素数間隔
        L1=[]                                       #要素数初期化
        
#---------------------------------グラフの描画例-----------------------------------#
    gs=gridspec.GridSpec(2,2)
    sel=plt.subplot(gs[0,0])
    merge=plt.subplot(gs[0,1])
    tim=plt.subplot(gs[1,0])
    bubble=plt.subplot(gs[1,1])
    
    sel.plot(sel_ele,sel_time,"r-")
    sel.set_title("sel_Sort")
    sel.set_xlabel('number of elements in a list')
    sel.set_ylabel('time(s)')
    
    merge.plot(merge_ele,merge_time,"r-")
    merge.set_title("merge_Sort")
    merge.set_xlabel('number of elements in a list')
    merge.set_ylabel('time(s)')
    
    tim.plot(tim_ele,tim_time,"r-",label="tim_Sort")
    tim.set_title("tim_Sort")
    tim.set_xlabel('number of elements in a list')
    tim.set_ylabel('time(s)')
    
    bubble.plot(bubble_ele,bubble_time,"r-")
    bubble.set_title("bubble_Sort")
    bubble.set_xlabel('number of elements in a list')
    bubble.set_ylabel('time(s)')
    
    plt.tight_layout()
    plt.show()

main()
