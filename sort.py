list = [3,9, 2, 7,5, 55 , 1 ,77, 56, 22, 4,10]

def BubbleSort(myList):
    x = 0
    while x < len(myList) - 1:
        first_number = myList[x]
        second_number = myList[x+1]
        if first_number > second_number:
            myList[x] = second_number
            myList[x+1] = first_number
            x = 0
        else:
            x +=1


    return(myList)

