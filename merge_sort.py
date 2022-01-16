def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new, sorted list
    
    Divide: find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    
    O(k log n) * O(n) = O(n log n)
    """
    
    if len(list) <= 1:
        return list
      
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)
  
def split(list):
    """
    Divides the unsorted list at midpoint into sublists
    Returns two sublists: left and right
    
    Takes O(log n)
    """
    
    # alternatively (to slicing), we can write two variables to keep track of the ends
    # of the new lists -- exercise
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    
    return left, right
  
def merge(right, left):
    """
    Merges two lists/arrays, sorting them in the process
    Returns new list
    
    O(n)
    """
    
    l = []
    i = 0 # indexes in left list
    j = 0 # indexes in right list
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[2:])

 