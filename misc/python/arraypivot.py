
"""
    Write a function that pivots an array of size n by k places.
    E.g. 12345 pivot 2 -> 45123
"""




''' Naive implementation of array pivot. O(n). '''
def pivotArrayNaive( intArray ,pivotPos ):

    LENGTH = len( intArray)
    
    if pivotPos == 0:
        return intArray

    if pivotPos >= LENGTH or pivotPos < 0:
        return -1

    
    pivotArray = [0] * LENGTH
    index = 0
    for num in intArray:
        pivotArray[ -LENGTH + pivotPos + index] = num
        index = index + 1

    return pivotArray



''' Second attempt, shooting for O( n log n) 
    This is probably not correct, don't know what python is doing behind the scenes.
    Will test. '''
def pivotArrayCons( intArray ,pivotPos):

    LENGTH = len( intArray)
    
    if pivotPos == 0:
        return intArray

    if pivotPos >= LENGTH or pivotPos < 0:
        return -1


    return intArray[-pivotPos:] + intArray[:LENGTH-pivotPos] 





arr = [1,2,3,4,5,6,7,8,9]

print( 
     pivotArrayNaive( arr ,0)
    ,pivotArrayNaive( arr ,2)
    ,pivotArrayNaive( arr ,5)
    ,pivotArrayNaive( arr ,9)
    ,pivotArrayNaive( arr ,-4)

)


print(
    pivotArrayCons( arr ,2)
)