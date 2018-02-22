from __future__ import division
import random

def getNumbers(a):
	num=[]
	for i in range(100):
		num.append(random.sample(a,5))	
	return num
def callNumbers(choice,a):
	x=[0]*80
	exit=True
	bingo=0
	while exit:
		bingo=bingo+1
		y=random.sample(a,1)
		a.remove(y[0])
		for i in range(0,80):
			if y[0] in choice[i]:
				x[i]+=1
				if x[i]==5:
					exit=False
	return bingo

bingos=0
for i in range(1000):
	a=range(1,81)
	players=getNumbers(a)
	bingos+=callNumbers(players,a)
print (bingos/1000)

 c=input("GTP")

