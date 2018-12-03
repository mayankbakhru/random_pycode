import random
list1 = list()
for x in range(5):
  hold = random.randint(1,71)  
  while hold in list1:
      hold = random.randint(1,71)
  list1.append(hold)
print (list1)
