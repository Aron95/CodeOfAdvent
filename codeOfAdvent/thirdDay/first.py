from typing import List
import logging



""" Configuartes the configuration that is been used to create the loggerfile"""
def initializeLogger():
    logging.basicConfig(filename='status.log', encoding='utf-8', level=logging.DEBUG)


""" Takes an string path argument to open a file reads it and trys to split it after every new line.
    Returns an list of strings """
def openFile(path:str)->List[str]:
    assert isinstance(path,str)
    
    with open(path) as file:
        file = file.read()
        try:#würde man des so machen?
            file = file.split("\n")
        except:
            print("Error")
    return file

""" Takes an list of strings and a count int variable. Counts in the given column every entry thats a '1'.
    If the result is higher then the length of the entry list divided by 2 it returns '1' else '0' """
def countMostCommonBit(data:List[str],count:int)->str:
    assert isinstance(data, list)
    assert isinstance(count,int)
    
    count = count
    myList = [item[count] for item in myList]
    result = myList.count("1")
    if result >= (len(myList)/2):
        return "1"
    else:
        return "0"
 
""" Takes an list of strings and a count int variable. Counts in the given column every entry thats a '1'.
    If the result is higher then the length of the entry list divided by 2 it returns '0' else '1' """   
def countLeastCommonBit(data:List[str],count:int)->str:
    assert isinstance(data, list)
    assert isinstance(count,int)
    
    count = count
    myList = [item[count] for item in myList]
    result = myList.count("1")
    if result >= (len(myList)/2):
        return "0"
    else:
        return "1"
    
""" Takes an list of string, bit string and a count int variable. If the value in the given column is not equal the bit,
    the entry will be dropped.
    Returns the new list"""
def deleteBitStrings(data:List[str], bit:str,count:int)->List[str]:
    assert isinstance(data, list)
    assert isinstance(bit,str)
    assert isinstance(count,int)
    
    #myList = [x if x[0] != bit  for x in myList] Nachschauen wie programmieren
    newList = []
    for x in mylist:
        if x[count] == bit:
            newList.append(x)
    return newList     


""" Takes a string list of the data and takes what kind of gas.
    As long as the list length is not 1 the list will be reduced by detecting the most common or least common bit
    and delet every entry that dose not match the required bit at the given row place. The row place is detected by a count
    variabel.
    Returns the last entry as a list"""       
def reduceBitString(data:List[str],gas:str)->List[str]:
    assert isinstance(data, list)
    assert isinstance(gas,str)
    
    count =0
    while(True):
        
        if gas == "oxy":
            logging.debug('Length of the bit list for oxy is:%s',len(data))
        
            if len(data) ==1:
                break
            data = deleteBitStrings(data,countMostCommonBit(data,count),count)
            count = count +1
            if count == 12:
                count=0
                
        elif gas == "o2":
            logging.debug('Length of the bit list for o2 is:%s',len(data))
        
            if len(data) ==1:
                break
            data = deleteBitStrings(data,countLeastCommonBit(data,count),count)
            count = count +1
            if count == 12:
                count=0
    return data


if __name__ =="__main__":
    initializeLogger()
    
    path ="/home/peter/Progamming/python/python_test/codeOfAdvent/thirdDay/input.txt"
    data=openFile(path)
    dataForO2 = reduceBitString(data,"o2")
    dataForOxy = reduceBitString(data,"oxy")
    
    logging.debug("O2 is: %s",dataForO2)
    logging.debug("Oxy is: %s",dataForOxy)


    print(int(dataForOxy[0],2)*(int(dataForO2[0],2)))


    


