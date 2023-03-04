# merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(lista, left, medium, right):
            list1 = lista[left:medium + 1]
            list2 = lista[medium + 1:right + 1]
            i = 0
            j = 0
            k = left
            while i < len(list1) and j < len(list2):
                if list1[i] <= list2[j]:
                    lista[k] = list1[i]
                    k += 1
                    i += 1
                else:
                    lista[k] = list2[j]
                    k += 1
                    j += 1
            while i < len(list1):
                lista[k] = list1[i]
                k += 1
                i += 1
            while j < len(list2):
                lista[k] = list2[j]
                k += 1
                j += 1
            
                
                    
                    
            
            
        def mergeSort(lista, left, right):
            if left < right:
                medium = (left + right) // 2 
                mergeSort(lista, left, medium)
                mergeSort(lista, medium + 1, right)
                merge(lista, left, medium, right)
        
        
        
        mergeSort(nums, 0, len(nums) - 1)
            
        return nums