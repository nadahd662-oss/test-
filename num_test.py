#import numpy as np 
#print(np.__version__)
'''
my_list = [1, 2, 3, 4]
my_list = my_list * 2
print(my_list)
'''
#array = np.array([1, 2, 3, 4])
#array *=2
#print(array)
#import numpy as np
'''
#array = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']],
                  [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']],
                  [['S', 'T', 'U'],['V', 'W', 'X'],['Y', 'Z', '']]])

#print(array.ndim)
#print(array.shape)
#print(array[1][1][1]) and we can code it as :
#print(array[1, 1, 1])

#exercice:

name = array[1, 1, 1] + array[0, 0, 0] + array[0, 1, 0] + array[0, 0, 0]
print(name)
'''

#SLICING: 
'''
import numpy as np
array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])
## array[start:end:step]

#print(array[:, 0]) #select every 1st character/columns of each row.
#print(array[:, 0:3]) # .. .. the first 3 columns .. .. .. 
print(array[::2])
'''
#COMPARISON OPERATORS 
'''
import numpy as np
scores = np.array([91, 55, 100, 73, 89, 62])
scores[scores < 60] = 0
print(scores)
#print(scores == 100)
#print(scores >= 60)
'''

#BROADCASTING
'''
array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array1 * array2)
'''
#FILTERING
'''
import numpy as np
ages = np.array([[17, 21, 18, 36, 19, 65],
                [39, 22, 15, 99, 39, 20]])

teens = ages[ages < 18] 
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65 ]
evens = ages[ages % 2 == 0 ]
odds = ages[ages % 2 != 0]

print(odds)
'''
          ## WHEN FUNCTION IN FILTERING : PRESERVE THE ORIGINAL SHAPE
           
import numpy as np
ages = np.array([[17, 21, 18, 36, 19, 65],
                [39, 22, 15, 99, 39, 20]])

adults = np.where(ages >= 18, ages, 'NV')
print(adults)

