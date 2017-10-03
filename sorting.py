# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:51:45 2017

@author: mashiksa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:30:03 2017

@author: mashiksa
"""

#Quick Sort
def partion(nums,wall,pivotloc):
    pivot = nums[pivotloc]
    cur = wall
    while cur < pivotloc:
        print(nums)
        print(cur)
        print(nums[cur])
        if nums[cur] < pivot:
            print("True")
            nums[cur], nums[wall] = nums[wall], nums[cur]
            wall += 1
        cur += 1
    nums[pivotloc], nums[wall] = nums[wall], nums[pivotloc]
    return wall+1         

def quicksort(nums, wall, pivotloc):
    if wall < pivotloc:
        p = partion(nums, wall, pivotloc)
        quicksort(nums, p, pivotloc)
        quicksort(nums, wall, p-1)

nums = [5,8,2,10,6,3,9,7]
pivotloc = len(nums)-1
wall = 0
res = partion(nums, wall, pivotloc)
res1 = partion(nums, res, pivotloc)
res2 = partion(nums, wall, res-1)

partion(nums, wall, res2)


len1 = 7
min1 = 0



#Selection Sort
def selsort(nums):
    len1 = len(nums)
    for i in range(len1):
        min1 = i
        for j in range(min1,len1):
            if nums[j] < nums[min1]:
                nums[j], nums[min1] = nums[min1], nums[j]
    return nums

        
def selsort_op(nums):
    len1 = len(nums)
    edge = len1-1
    for i in range(len1):
        min1 = i
        for j in range(min1,edge):
            if nums[j] < nums[min1]:
                nums[j], nums[min1] = nums[min1], nums[j]
            if nums[j] > nums[edge]:
                nums[j], nums[edge] = nums[edge], nums[j]
        edge -= 1
    return nums

    
    
    
    
import timeit        
import random
import time

arr = [random.randint(0,1000000) for i in range(0,10000)]
start = time.clock()
res1 = selsort(arr)
end = time.clock()
dif1 = end-start

start = time.clock()
res2 = selsort_op(arr)
end = time.clock()
dif2 = end-start

randomcheck = [random.randint(0,1000) for i in range(0,100)]
[res1[randomcheck[i]] == res2[randomcheck[i]] for i in range(10)]
 
 nums = arr
def counting_sort(nums):
    min_val = min(nums)
    max_val = max(nums)
    uni_val = list(range(min_val, max_val+1))
    count_val = [nums.count(uni_val[i]) for i in range(max_val-min_val)]
                 
nums1 = [1,2,4,5]
nums2 = [3,6,7,8]
res = []

nums1 = [1,2]
nums2 = [3,4]

#Merge Sort Median
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



#anagram Check


def strdict(word):
    word = word.replace(' ',"")
    word = list(word)    
    res = {}
    for w in word:
        try:
            res[w] = res[w] + 1
        except:
            res[w] = 1
    return res
    
   

def anag(check1, check2):   
    if(len(strdict(check1).items() & strdict(check2).items()) == len(strdict(check1).items() | strdict(check2).items())):
        return True
    else:
        return False
        
s = "anagram"
t = "nagaramm"

strdict(s).items() & strdict(t).items()


cmp(list(s),list(t))    
        
nums = [3,2,2,3]
val = 3

[i for i in list(nums) if i != val]
 
 
 #Permutation & Combination...
 def permute(a, l, r,i):
    print("Iter Id :%d l:%d"%(i,l))
    if l==r:
        print("Res  %s"%(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, i)
            a[l], a[i] = a[i], a[l] # backtrack
            

string = "123"
n = len(string)
a = list(string)
permute(a, 0, n-1, 0)



# Binary Search Tree

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)    
    
    
r = Node(3)

r.data

class node:
    def __init__(self,val, next = None):
        self.next = next
        self.val = val
        
r = node(3)
head = node(4, r)


def fib(n):
    res = [0,1]
    for i in range(n+1):
        res.append(res[i] + res[i+1])       
    return res[n]

def fibsum(n):
    res = [0,1]
    i = 0
    while True:
        val = res[i] + res[i+1]
        if val > n:
            break
        res.append(res[i] + res[i+1])
        i += 1
    res1 = [i for i in res if i%2 == 0]
     return sum(res1)
        
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

    

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
c = ListNode(2)
c = ListNode(4,c)
c = ListNode(3,c)

d = ListNode(5)
d = ListNode(6,d)
d = ListNode(4,d)

root = n = ListNode(10)
n.next = ListNode(11)
c.val
c.next.val
c.next.next.val

l1 = c
l2 = d
i = 0
#res = ListNode(None)
res = ''
while l1:
    val = l1.val + l2.val + i
    print(val)
    if val > 9:
        i = 1
        val = 0
    else:
        i = 0
    l1 = l1.next
    l2 = l2.next
#    print(val)
    if res:
        res = ListNode(val, res)
    else:
        res = ListNode(val)        

        
def print1(va):
    while va:
        print(va.val)
        va = va.next
    

#Adding Two Linked List
        
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    i = 0
    root = res = ListNode(None)
    while l1 or l2 or i != 0:
        v1, v2 = (0, 0)
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        val = v1 + v2 + i     
        i, val = divmod(val, 10)
        res.next = ListNode(val)
        res = res.next
    return root.next
    
    
    
    
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None





r =  ListNode(20)



#find prime numbers
import sys

if sys.version_info[0] == 3:
    xrange = range

max_n = 100
numbers = list(xrange(3, max_n+1, 2))
half = (max_n)//2
initial = 4

for step in xrange(3, max_n+1, 2):
    for i in xrange(initial, half, step):
        numbers[i-1] = 0
    initial += 2*(step+1)

    if initial > half:
        x = [2] + filter(None, numbers)

        
        
a = [1,2,3,4,5,6]



def ret(item, loc):
    if loc == len(item)-1:
        print(item[loc])
    else:
        i = loc + 1
        print(item[loc])
        ret(item, i)
        
       
def sumof(n):
    if n != 0:
        return(n + sumof(n-1))
    else:
        return(n)
        
def sumof(n):
    if n != 0:
        return(n * sumof(n-1))
    else:
        return(1)
        
        
a = [0,1,2,2,1,0,0,1,2,314,1,12,1,123123,0]

       
def pr(x,n):
    if n == 0:
        return 1 if x[n] == 0 else 1
    else:
        return(pr(x,n)+pr(x,n-1))
