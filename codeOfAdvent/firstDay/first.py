# takes data from the file and creates a list, splitting every \n

myFile = open("/home/peter/Progamming/python/python_test/codeOfAdvent/firstDay/firstInput.txt", "r")
data = myFile.read()
dataIntoList = data.split("\n")
print(dataIntoList)
myData = [int(x) for x in dataIntoList if x != '']



def compair(myData):
    counter =0
    boolResult = [int(sub1) < int(sub2) for sub1, sub2 in zip(myData, myData[1:])]

    for x in boolResult:
        if x ==True:
            counter += 1
    return counter

print(compair(myData))



