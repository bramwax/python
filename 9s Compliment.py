numA = 131
numB = str(25)
ninesComp = ""
for i in range(len(numB)):
    counter = 0
    while counter + int(numB[i]) < 9:
        counter += 1
    ninesComp += str(counter)
ninesComp = str(int(ninesComp) + numA)
ninesComp = int(ninesComp[1:]) + int(ninesComp[:1])

print(ninesComp)
