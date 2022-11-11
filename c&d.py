import random
score = 0
list = ['aluminum foil','rubber','water','copper','silicone','a PVC pipe','paper','glass']
'aluminum foil' == 'conductor'
'rubber' == 'insulator'
'water' == 'insulator'
'copper' == 'conductor'
'silicone' == 'insulator'
'a PVC pipe' =='insulator'
'paper' == 'insulator'
'glass' == 'insulator'
node = random.choice(list)
anwser = input("is {} a conductor or an insulator?".format(node))
#haven't coded right
if anwser == True: score =+ 1
print(score)
