
'''
In Python, when an array is created, a reference to the values are stored in a contiguous structure in memory.


Inserting items in an array can be done in 2 ways:
. inserting by index: adding an element to an array with its index. Its a linear runtime operation. 
. using append method, ie inserting item to the bottom of an array. Its an amortized constant time operation. 
This operation happens under the hood of python. Ideally calling append on an array at some point calls a 
resize operation on the array. This operation adds additional space to the initial space in this order: 
0,4,8,16,25,35,46,...

Accessing Values: Has a constant time. 

Deleting an item: Just like inserting, its a linear runtime operation

Updating a value: Its a constant time operation

Extend method: has a runtime of O(k) where k is the number of items in the passed array. Since this basically calls
append on each item in the passed array.

so for each array operation, know the how the new value relates the old values to determine the runtime of that
operation.
'''

old_array = [1,2,4]
new_arr = [5,6,7,8]
new_arr.extend(old_array)

print(new_arr[4])