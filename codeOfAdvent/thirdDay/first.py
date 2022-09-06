path = "/home/peter/Progamming/python/python_test/codeOfAdvent/thirdDay/input.txt"

zero =0
one =0

with open(path) as f:
    data = f.read()
    data =  data.split("\n")


d = dict.fromkeys(list(range(1,13)),0)




print(data)