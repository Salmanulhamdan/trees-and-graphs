def binarysearch(arr,element):
    length=len(arr)

    if length <= 0:
        return -1
    pivet=arr[length//2]
    left=arr[:length//2]
    right=arr[length//2 + 1:]
   

    if  pivet==element:
       
        return True

    elif pivet > element:
        # print("pivet is high")

        return binarysearch(left,element)
    else:
        # print("pivet is low")

        return binarysearch(right,element)
    


    # low=0
    # high=len(arr)-1

    

    # while low <= high:
    #     mid=(low+high)//2

    #     if arr[mid]==element:
    #         return True
        
    #     elif arr[mid]>element:
    #         high=mid-1

    #     else:
    #         low=mid+1
    # return -1







ar=[1,3,4,5,6,7,8]

print(binarysearch(ar,3))


