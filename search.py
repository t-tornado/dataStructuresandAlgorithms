def lin_search(list, target):
    '''
    return the index of the target value if value is founc or -1 if value is not found.
    '''
    for i in range(0, len(list)):
        if(list[i] == target):
            return i
    return -1

def verify(result):
    if(result >= 0):
        print("Value is in the list")
    else:
        print("Value is not in the list")



def binary(list, target):
    '''
    set pointers: first and last indexes
    in a loop:
    find middle value and compare to the target.
    if target is equal to the mid-item, return item
    else:
        if the midpoint value is less than target, set the first to the midpoint + 1
        else set the last value to the midpoint - 1

    return -1 after the loop completes
    '''
    first_index = 0
    last_index = len(list) - 1
    while (first_index <= last_index):
        midpoint = (first_index + last_index)//2
        if(list[midpoint] == target):
            return midpoint
        else:
            if(list[midpoint] < target):
                first_index = midpoint + 1
            elif(list[midpoint] > target):
                last_index = midpoint - 1
    return -1

def rec_binary(list, target):
    '''
    using recurssion to implement a binary search to identify whether a value is in a list or not.
    algorithm.
    . set base case: if the array is empty, return False
    . else:
        .. get the midpoint of the current list.
                ... if the midpoint value is the target value, return True.
                ... else:
                    .... if midpoint value is less than the target, make a recursive call and pass a slice of the
                    array from midpoint + 1 to the end and target
                    ... else make recursive call and pass a slice of array from the beginning to midpoint - 1 and target
    '''
    print('')
    print(list)
    print(target)
    if(len(list) == 0):
        return  False
    else:
        midpoint = (len(list))//2
        print('MDP  ',midpoint)
        if(list[midpoint] == target):
            return True
        else:
            if(list[midpoint] > target):
                return rec_binary(list[:midpoint], target)
            else:
                return rec_binary(list[midpoint:], target)

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
result = binary(nums, 1)
boolean_result = rec_binary(nums, 11)
print(boolean_result)