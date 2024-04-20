a = [ [2, 4, 6, 8 ],  
    [ 1, 3, 5, 7 ],  
    [ 8, 6, 4, 2 ],  
    [ 7, 5, 3, 1 ] ]  
          
# for i in range(len(a)) :  
#     for j in range(len(a[i])) :  
#         print(a[i][j], end=" ") 
#     print()

# print(a[3][3])

# print (len(a))

# print(len(a[0]))

# b=[[0,1,0,1,0],[1,0,0,1,1],[1,1,1,0,1]]

# print (len(b))

# print(len(b[0]))



def findDiagonalOrder( nums):
    diagonals = {}
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if i + j not in diagonals:
                diagonals[i + j] = []
            diagonals[i + j].append(nums[i][j])
            # print(diagonals)

    result = []
    for k in range(len(diagonals)):
        print(diagonals[k] )
        result.extend( reversed(diagonals[k]))

    return result

nums = [[1,2,3],[4,5,6],[7,8,9]]



a=findDiagonalOrder(nums)
print(a)

