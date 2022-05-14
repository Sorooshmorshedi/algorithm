from sort import BubbleSort

list = [3,9, 7,5, 55 , 1 ,77, 56, 22, 4,10]
x = 77


def LineSearch(myList, lookFor):
    result={'find': False, 'possition': None}
    for index in range(0, len(myList)):
        if myList[index] == lookFor:
            result['find'] = True ; result['possition'] = index+1
    return(result)

def BinarySearch(myList, lookFor, step=0):
    try:
        result={'find': False}
        myList = BubbleSort(myList)
        index = int(len(myList) / 2)
        if myList[index] == lookFor:
            result['find'] = True
            print(result)
        elif myList[index] > lookFor:
            new_list = []
            for i in range(0, index):
                new_list.append(myList[i])
            BinarySearch(new_list, lookFor)
        elif myList[index] < lookFor:
            new_list = []
            for i in range(index+1, len(myList)):
                new_list.append(myList[i])
            BinarySearch(new_list, lookFor, index)
    except:
        print(result)
