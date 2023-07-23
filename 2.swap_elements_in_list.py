def swaplist(newlist,pos1,pos2):
    temp = newlist[pos1-1]
    newlist[pos1-1] = newlist[pos2-1]
    newlist[pos2-1] = temp
    return newlist

print(swaplist([1,2,3,4,5,6,7],pos1=4,pos2=5))


def swapPositions(list, pos1, pos2):
    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)

    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))