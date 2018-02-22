RomanMilestoneNum=['I','V','X','L','C','D','M','-V','-X','-L','-C','-D']
AkeraioiArithmoi =[1,5,10,50,100,500,1000,5000,10000,50000,100000,500000]

def lala(arith,y):
   g=0
   c=2*y -1
   latin=""
   while c >= 0:
      
      if ((arith // AkeraioiArithmoi[c]) == 0) :
         c = c - 1
      if ((arith // AkeraioiArithmoi[c]) == 1):
         if (arith + AkeraioiArithmoi[c-1] >= AkeraioiArithmoi[c+1]):
            latin += RomanMilestoneNum[c-1] + RomanMilestoneNum[c+1]
            arith=arith-(AkeraioiArithmoi[c-1] + AkeraioiArithmoi[c+1])
            c-=1
         else:
            latin += RomanMilestoneNum[c]
            arith=arith-AkeraioiArithmoi[c]
            c-=1
      if ((arith // AkeraioiArithmoi[c]) == 2):
         latin += 2 * RomanMilestoneNum[c]
         arith=arith-AkeraioiArithmoi[c]
         c-=1
      if ((arith // AkeraioiArithmoi[c]) == 3):
         latin += 3 * RomanMilestoneNum[c]
         arith=arith-AkeraioiArithmoi[c]
         c-=1
      if ((arith // AkeraioiArithmoi[c]) == 4):
         latin += RomanMilestoneNum[c] + RomanMilestoneNum[c+1]
         arith=arith-AkeraioiArithmoi[c]
         c-=1
      if ((arith // AkeraioiArithmoi[c]) == 5):
         arith=arith-AkeraioiArithmoi[c]
         latin +=RomanMilestoneNum[c]
         c -=1
         
         

   return latin

arithmos=int(input("Give me a number:"))
x=len(str(arithmos))
print (lala(arithmos,x))
