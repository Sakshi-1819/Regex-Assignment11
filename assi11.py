#!/usr/bin/env python
# coding: utf-8

# # Q1.Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element).

# In[3]:


def minJumps(arr, l, h):
    if (h == l):
        return 0

    if (arr[l] == 0):
        return float('inf')

    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + arr[l] + 1):
            jumps = minJumps(arr, i, h)
            if (jumps != float('inf') and
                    jumps + 1 < min):
                min = jumps + 1

    return min

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, 0, n - 1))


# In[7]:


def minJumps(arr, l, h):
    if (h == l):
        return 0

    if (arr[l] == 0):
        return float('inf')

    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + arr[l] + 1):
            jumps = minJumps(arr, i, h)
            if (jumps != float('inf') and
                    jumps + 1 < min):
                min = jumps + 1

    return min

arr = [1, 4, 3, 2, 6, 7]
n = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, 0, n - 1))


# # Q2. Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

# In[6]:


def printPairs(arr, n, k):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == k):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep="")

arr = [1, 5, 7, 1]
n = len(arr)
k = 6
printPairs(arr, n, k)


# In[9]:


def printPairs(arr, n, k):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == k):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep="")

arr = [1, 1, 1, 1]
n = len(arr)
k = 2
printPairs(arr, n, k)


# # Q3.Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m.Task is to check whether a2[] is a subset of a1[] or not.Both the arrays can be sorted or unsorted.It may be assumed that elements in both array are distinct.

# In[10]:


def isSubset(arr1, arr2, m, n):
    i = 0
    j = 0
    if m < n:
        return 0

    arr1.sort()
    arr2.sort()

    while i < n and j < m:
        if arr1[j] < arr2[i]:
            j += 1
        elif arr1[j] == arr2[i]:
            j += 1
            i += 1
        elif arr1[j] > arr2[i]:
            return 0
    return False if i < n else True


# Driver code
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

m = len(arr1)
n = len(arr2)
if isSubset(arr1, arr2, m, n) == True:
    print("arr2 is subset of arr1 ")
else:
    printf("arr2 is not a subset of arr1 ")


# In[11]:


def isSubset(arr1, arr2, m, n):
    i = 0
    j = 0
    if m < n:
        return 0

    arr1.sort()
    arr2.sort()

    while i < n and j < m:
        if arr1[j] < arr2[i]:
            j += 1
        elif arr1[j] == arr2[i]:
            j += 1
            i += 1
        elif arr1[j] > arr2[i]:
            return 0
    return False if i < n else True


# Driver code
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 2, 4]

m = len(arr1)
n = len(arr2)
if isSubset(arr1, arr2, m, n) == True:
    print("arr2 is subset of arr1 ")
else:
    printf("arr2 is not a subset of arr1 ")


# In[13]:


def isSubset(arr1, arr2, m, n):
    i = 0
    j = 0
    if m < n:
        return 0

    arr1.sort()
    arr2.sort()

    while i < n and j < m:
        if arr1[j] < arr2[i]:
            j += 1
        elif arr1[j] == arr2[i]:
            j += 1
            i += 1
        elif arr1[j] > arr2[i]:
            return 0
    return False if i < n else True


# Driver code
arr1 = [10, 5, 2, 23, 19]
arr2 = [19, 5, 3]

m = len(arr1)
n = len(arr2)
if isSubset(arr1, arr2, m, n) == True:
    print("arr2 is subset of arr1 ")
else:
    print("arr2 is not a subset of arr1 ")


# # Q4. Number Series with a Twist Consider the series : 0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8. This series is a mixture of 2 series, all the odd terms in this series form even numbers in ascending order and every even terms is derived from the previous term using the formula (x/2) Write a program to find the nth term in this series.

# In[15]:


n = int(input('enter the number:'))
a=0
b=0
for i in range(1,n+1):
    if(i%2!=0):
        a= a+2
    else:
        b= b+1
if(n%2!=0):
    print('{}'.format(a-2))
else:
    print('{}'.format(b-1))


# In[ ]:




