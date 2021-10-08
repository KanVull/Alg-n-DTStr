import random as rnd

def quick_sort(array):  

    def partition(array, left, right):  
        x = rnd.choice( array[left:right] )
        i, j = left, right
        while True:
            while array[i] < x: i += 1
            while array[j] > x: j -= 1

            if i >= j:  return j

            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    def _quick_sort(array, left, right):
        if left < right:
            split_index = partition(array, left, right)
            _quick_sort(array, left, split_index)
            _quick_sort(array, split_index + 1, right)

    _quick_sort(array, 0, len(array) - 1)


array = [rnd.randrange(0,100) for _ in range(20)]
quick_sort(array)  
print(array) 