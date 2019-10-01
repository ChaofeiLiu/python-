#体育竞技问题.py
from random import random
def printInfo():
    print("这个程序模拟两个选手a和b的某种竞技比赛")
    print("程序运行需要两个选手的能力值（0到1之间的小数表示）")

def getInputs():
    a=eval(input("请输入选手a的能力值（0—1）:"))
    b=eval(input("请输入选手b的能力值（0—1）:"))
    n=eval(input("请输入模拟比赛的场次:"))
    return a,b,n

def gameover(a,b):
    return a==15 or b==15

def simOnegames(proba,probb):
    scorea,scoreb=0,0
    serving="A"
    while not gameover(scorea,scoreb):
        if serving=="A":
            if random()<proba:
                scorea+=1
            else:
                serving="B"
        else:
            if random()<probb:
                scoreb+=1
            else:
                serving="A"
    return scorea,scoreb

def printSummary(winsa,winsb):
    n=winsa+winsb
    print("竞技比赛开始，共模拟{}场比赛".format(n))
    print("选手a获胜的场数是：{},占比{:0.1%}".format(winsa,winsa/n))
    print("选手b获胜的场数是：{},占比{:0.1%}".format(winsb,winsb/n))

def simNgames(n,proba,probb):
    winsa,winsb=0,0
    for i in range(n):
        scorea,scoreb=simOnegames(proba,probb)
        if scorea>scoreb:
            winsa+=1
        else:
            winsb+=1
    return winsa,winsb

def main():
    printInfo()
    proba,probb,n=getInputs()
    winsa,winsb=simNgames(n,proba,probb)
    printSummary(winsa,winsb)

main()
    

        
