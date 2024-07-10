# Selection sort {select min and swap}

class Solution: 
    def select(self, arr, i):
        min = i 
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        return min
    
    def selectionSort(self, arr,n):
        for i in range(n):
            min = self.select(arr,i)
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(n-1,-1,-1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

def insertion_sort(arr,n):
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -= 1
    return arr

# MergeSort 
class Solution:
    def merge(self,arr, l, m, r): 
        temp = []
        left = l
        right = m+1
        while left<=m and right<=r:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        
        while left<=m:
            temp.append(arr[left])
            left+=1
        while right<=r:
            temp.append(arr[right])
            right+=1
        
        for i in range(l,r+1):
            arr[i] = temp[i-l]
            
    def mergeSort(self,arr, l, r):
        if l >= r:
            return 
        mid = (l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)
