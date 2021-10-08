import random as rnd

def quick_sort(array):  
    # Функция сортировки массива

    def partition(array, left, right): 
        # Функция выбора случайного элемента-разделителя массива 
        # (части массива от left границы до right границы) на 
        # две части 
        x = rnd.choice( array[left:right] ) # Выбираем случайное число в части массива
        while True:
            while array[left] < x: left += 1    #   Пока "левый" элемент меньше, чем случайно выбранный, сдвигаем границу
                                                #   Ищем элемент, который будет больше x    
            while array[right] > x: right -= 1  #   Такая же ситуация только с другой стороны

            if left >= right:  return right     #   Прерываем цикл и возвращаем новую границу-разделитель массива

            array[left], array[right] = array[right], array[left] # Меняем местами левое и правое число - таким образом справа от "x" 
                                                                  # будет число больше "х", а слева меньше
            left, right = left + 1, right - 1   #   Сдвигаем границы для поиска новых элементов, не проходящих по условию
                                                #   слева от х числа меньше х, а справа больше

    def _quick_sort(array, left, right):
        # Функция для запуска рекурсивной сортировки для выбранной области массива
        if left < right: # условие продолжения рекурсии
            split_index = partition(array, left, right)
            _quick_sort(array, left, split_index)
            _quick_sort(array, split_index + 1, right)

    _quick_sort(array, 0, len(array) - 1)


array = [rnd.randrange(0,100) for _ in range(20)]
quick_sort(array)  
print(array) 