 #Based on this list of tuples: 
lt = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

desired_result = [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]

#Sort the list so the result looks like this: [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]
#This is first sorted by the last element in the tuple and then the first element in the tuple. You should do this in 1 step, but it might help you to try it out in 2 steps first

print(f'Unsorted list: {lt}')

print(f'Sorted list: {sorted(lt)}')

ltnew = sorted(lt, key= lambda x: (x[1], x[0])) #Key = function returning two values x[1] and x[0]
print(f'Sorted by value index[1] then index[0]: {ltnew}')

if ltnew == desired_result:
    print('SUCCESS!!!')