# O(nlogn)
def main() :
    list1 = [5,4,3,2,1,1,1,-1,-2,-3,-4]
    print(merge(list1))

def merge(list1) :
    if len(list1) > 1 :
        mid = len(list1) //2
        left = list1[:mid]
        right = list1[mid:]

        merge(left)
        merge(right)

        i=0
        j=0
        k=0

        print(f"left: {left} and right: {right}")
        while i < len(left) and j < len(right) :
            if left[i] < right[j] :
                list1[k] = left[i]
                i+=1
            else :
                list1[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left) :
            list1[k] = left[i]
            i+=1
            k+=1

        while j < len(right) :
            list1[k] = right[j]
            j+=1
            k+=1
            
    return list1
                
main()