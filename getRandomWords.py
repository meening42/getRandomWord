
import random

with open('seedWordsList.txt') as f:
    lines = f.readlines()
	
len(lines)
print(len(lines))
	
for x in  range(12):	
	print(lines[random.randint(0,len(lines))])