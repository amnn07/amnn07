#main
TTT=[0,0,"0",0,"0","0",'0','0',0]
print('''         1|2|3
         4|5|6
         7|6|9''')
print("----- 1 for 'O' -----")
print("----- 2 for 'X' -----")
def p_w():
   if(TTT[0]==TTT[1]==TTT[2]):
      return 0
   elif(TTT[3]==TTT[4]==TTT[5]):
      return 0
   elif(TTT[6]==TTT[7]==TTT[8]):
      return 0
   elif(TTT[0]==TTT[3]==TTT[6]):
      return 0
   elif(TTT[1]==TTT[4]==TTT[7]):
      return 0
   elif(TTT[2]==TTT[5]==TTT[8]):
      return 0
   elif(TTT[0]==TTT[4]==TTT[8]):
      return 0
   elif(TTT[2]==TTT[4]==TTT[6]):
      return 0
   else:
      return 1
for i in range(0,9):
   if(i%2==0):
      print("--:player one turn:--")
      pos=int(input("enter the poistion for X : "))
      for j in range(0,10):
         if(pos==j):
            TTT[j-1]=1
            print(TTT[0:3])
            print(TTT[3:6])
            print(TTT[6:10])
            break
      else:
         print("-----:::enter correct postion:::-----")
      win=p_w()
      if(win==0):
         print(":*:*:*:*:*:*:*:player one is winner:*:*:*:*:*:*:")
         break
   else:
      print("---::player two turn::---")
      pos=int(input("enter the poistion for O : "))
      for k in range(0,10):
         if(pos==k):
            TTT[k-1]=2
            print(TTT[0:3])
            print(TTT[3:6])
            print(TTT[6:10])
            break
      else:
         print("-----:::enter correct postion:::-----")
      win=p_w()
      if(win==0):
         print(":*:*:*:*:*:player two is winner:*:*:*:*:*:*:")
         break
   
   
