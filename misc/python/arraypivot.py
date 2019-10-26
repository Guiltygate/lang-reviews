
"""
    Write a function that pivots an array of size n by k places.
    Assuming a right pivot.
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



''' Different version, more concise, but only because of python. Mechanically is about the same, since Python should be copying values from
    the array into new arrays.'''
def pivotArrayCons( intArray ,pivotPos):

    LENGTH = len( intArray)
    
    if pivotPos == 0:
        return intArray

    if pivotPos >= LENGTH or pivotPos < 0:
        return -1


    return intArray[-pivotPos:] + intArray[:LENGTH-pivotPos] 




def printTest():
    arr = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]

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



def sizeTest():
    arr = [1 for i in range(1000000)]

    pivotArrayNaive( arr ,90)
    print( "Between")
    pivotArrayCons( arr ,90)



printTest()
sizeTest()

