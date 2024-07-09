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



