# Write code below 💖
h=0
s=0
r=0
g=0

ans=int(input('''Do you like Dawn or Dusk? 
1) Dawn 2) Dusk'''))
if(ans==1):
  print("gry and raven got +1")
  g+=1 
  r+=1
elif(ans==2):
  print("huffle and slytherin got +1")
  h+=1
  s+=1
else:
  print("enter a valid choice")
      
ans1=int(input('''Q2) When Im dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold'''))
if(ans1==1):
  print("hufflepuff got +1")
  h+=1
elif(ans1==2):
  print(" slytherin got +1")
  s+=1
elif(ans1==3):
  print(" ravenclaw got +1")
  r+=1
elif(ans1==4):
  print(" gryffindor got +1")
  g+=1
else:
  print("enter a valid choice")
      

ans2=int(input('''Q3) Which kind of instrument most pleases your ear?
 1) The violin
 2) The trumpet
 3) The piano
 4) The drum'''))
if(ans2==2):
  print("hufflepuff got +1")
  h+=4
elif(ans2==1):
  print(" slytherin got +1")
  s+=4
elif(ans2==3):
  print(" ravenclaw got +1")
  r+=4
elif(ans2==4):
  print(" gryffindor got +1")
  g+=4
else:
  print("enter a valid choice")
  
print("thanks for playing the game")
print(f"The score of slytherin is {s}.The score of slytherin is {s}.The score of ravenclaw is {r}.The score of gryffindor is {g}.")
if(s>h and  s>r and s>g):
  print(f"the highest score {s} is of slytherin ")
elif(h>s and h>r and h>g):
  print(f"the highest score {h} is of hufflepuff")
elif(r>s and r>h and r>g):
  print(f"the highest score {r} is of ravenclaw")
else:
   print(f"the highest score {g} is of gryffindor")
