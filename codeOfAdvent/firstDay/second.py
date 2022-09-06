counter =0
myFile = open("/home/peter/Progamming/python/python_test/codeOfAdvent/firstDay/firstInput.txt", "r")
data = myFile.read()
dataIntoList = data.split("\n")
myData = [int(x) for x in dataIntoList if x != '']

list1 = [1,2,3,4,5]
zipper= list(zip(myData,myData[1:],myData[2:]))

result = [sum(line) for line in zipper]

#print(zipper)
#print(result)

def compair(myData):
    counter =0
    boolResult = [int(sub1) < int(sub2) for sub1, sub2 in zip(myData, myData[1:])]

    for x in boolResult:
        if x ==True:
            counter += 1
    return counter

print(compair(result))