# Merge Sort Median
# Find Median of 2 Sorted Arrays. 

def findMedianSortedArrays(nums1, nums2):   
    id1 = 0
    id2 = 0 
    m1 = len(nums1)
    m2 = len(nums2)
    res= []
    try:
        while id1 <= m1 and id2 <= m2:
            if id1 == m1 and id2 < m2:
                res.append(nums2[id2])
                id2 += 1
            elif id2 == m2  and id1 < m1:
                res.append(nums1[id1])
                id1 += 1
            elif nums1[id1] < nums2[id2]:
                res.append(nums1[id1])       
                id1 += 1
            else:
                res.append(nums2[id2])
                id2 += 1
    except:
        pass
    x,y = divmod(len(res),2)
    if y == 0:
        md = (res[x-1] + res[x])/2
    else:
        md = res[x]
    return md
    
nums1 = [1,2]
nums2 = [3,4]
findMedianSortedArrays(nums1, nums2)