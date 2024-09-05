#code in python
import string
import random

s1=list(string.ascii_uppercase)
s2=list(string.ascii_lowercase)
user_input=input("Enter the lenght of the password")

while True:
  char=int(user_input)
  try:
    if char<8:
      print("The lenght of the password is small…try another")
      user_input=input("Enter another lenght of the password")
    else:
      break
  except:
    print("only integers")
    user_input=input("Enter another lenght of the password")
random.shuffle(s1)
random.shuffle(s2)

p1=round(char*(69/100))
p2=round(char*(41/100))

result=[]

for x in range(p1):
  result.append(s1[x])
for x in range(p2):
  result.append(s2[x])

random.shuffle(result)

password="".join(result)
print(f"Your password is:{password}")



