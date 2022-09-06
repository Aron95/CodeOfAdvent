

path = "/home/peter/Progamming/python/python_test/codeOfAdvent/secondDay/input.txt"

horizontalPosition =0
depth =0


with open(path) as f:
    data = f.read()
    data =  data.split("\n")

#list1 = ['down 2', 'up 3']

_2dList = [i.split(' ') for i in data]

for key,value in _2dList:
    if(key=="forward"):
        horizontalPosition += int(value)
    elif(key =="up"):
        depth -= int(value)
    elif(key=="down"):
        depth += int(value)

result = depth * horizontalPosition

print(result)

    

