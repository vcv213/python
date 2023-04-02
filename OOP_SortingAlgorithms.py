# Object Oriented Sorting algorithms #

class Sorting:

    def __init__(self, array1):
        self.list1 = array1

    ########## MERGE SORT ###########
    # Best Case: O(n log n)
    # Worst Case: O(n log n)
    def mergeSort(self) :
        if len(self.list1) > 1 :
            mid = len(self.list1)//2
            left = self.list1[:mid]
            right = self.list1[mid:]

            leftSort = Sorting(left)
            rightSort = Sorting(right)
            
            leftSort.mergeSort()
            rightSort.mergeSort()

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right) :
                if left[i] < right[j] :
                    self.list1[k] = left[i]
                    i+=1

                else :
                    self.list1[k] = right[j]
                    j+=1
                k+=1

            while i < len(left) :
                self.list1[k] = left[i]
                i+=1
                k+=1

            while j < len(right) :
                self.list1[k] = right[j]
                j+=1
                k+=1

        return self.list1
    
    ########## QUICK SORT ###########
    # Best Case: O(n log n)
    # Worst Case: O(n^2)    
    def quickSort(self) :
        if len(self.list1) > 1 :
            pivot = len(self.list1)//2
            lows = []
            highs = []
            
            for i in range(len(self.list1)) :
                if i != pivot :
                    if self.list1[i] < self.list1[pivot] :
                        lows.append(list1[i])
                    else :
                        highs.append(list1[i])
            
            lows_list = Sorting(lows)
            highs_list = Sorting(highs)
            
            lows_list.quickSort()
            highs_list.quickSort()
            
            self.list1[:] = lows + [self.list1[pivot]] + highs
            
            return self.list1
    
    ########## BUBBLE SORT ###########
    # Best Case: O(n)
    # Worst Case: O(n^2)
    def bubbleSort(self) :
        for i in range(len(self.list1)-1) :
            for j in range(len(self.list1)) :
                if self.list1[i] < self.list1[j] :
                    self.list1[i], self.list1[j] = self.list1[j], self.list1[i]

        return self.list1


if __name__ == '__main__' :

    list1 = Sorting([5,4,3,2,1,1,1,-1,-2,-3,-4])
    print("QuiskSorted List: ", list1.mergeSort())
    
    list2 = Sorting([5,4,3,2,1])
    print("MergeSorted List: ", list2.mergeSort())
    
    list3 = Sorting([9,8,7,6,5,4])
    print("BubbleSorted List: ", list3.bubbleSort())