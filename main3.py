class Node:
    def __init__(self, data: any) -> None:
        # Хранит информацию о данных в ячейке и две соседние ячейки
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> any:
        return str(self.data)    

class DoubleLinkedList:
    def __init__(self) -> None:
        self.lenght = 0
        self.head = None
        self.tail = None

    def __createList(self, node: Node) -> None:
        # Добавить первый элемент в список
        self.head = node
        self.tail = node
        self.head.next = node
        self.head.prev = node
        self.tail.next = node
        self.tail.prev = node
        return None

    def append(self, value: any) -> None:
        node = Node(value)
        if self.head:
            # Если список уже не пустой
            self.tail.prev = node
            self.head.next = node
            node.next = self.tail
            node.prev = self.head
            self.head = node            
        else:
            self.__createList(node)  

        self.lenght += 1
        return None

    def appendleft(self, value: any) -> None:
        node = Node(value)
        if self.head:
            self.head.next = node
            self.tail.prev = node
            node.next = self.tail
            node.prev = self.head
            self.tail = node            
        else:
            self.__createList(node)  

        self.lenght += 1
        return None

    def insert(self, value: any, index: int) -> None:
        # Вставляет новую ячейку в список по указанному индексу
        if index > self.lenght or index < 0:
            raise IndexError('List index out of range')
        if index == 0:
            self.appendleft(value)
            return None
        elif index == self.lenght:
            self.append(value)
            return None

        newNode = Node(value)
        node = self.tail
        # Начинаем считать ячейки начиная с хвоста
        currentIndex = 0
        while currentIndex != index:
            # Ищем ячейку с указанным индексом
            node = node.next
            currentIndex += 1
        # Вставляем на его место новую ячейку    
        newNode.next = node
        newNode.prev = node.prev    
        node.prev.next = newNode
        node.prev = newNode

        self.lenght += 1
        return None

    def index(self, value: any) -> int:
        # Поиск элемента в ячейках списка
        # Если соответствующего элемента не удаётся найти в списке возвращаем -1
        if self.lenght == 0:
            return -1
        currentIndex = 0
        node = self.tail
        while currentIndex < self.lenght:
            if node.data == value:
                return currentIndex
            currentIndex += 1
            node = node.next    
        else:
            return -1        

    def pop(self) -> object:
        if self.lenght == 0:
            # Нечего удалять, список пустой
            return None

        data = self.head.data
        if self.lenght == 1:
            # Затираем информацию о голове и хвосте списка
            self.head = None
            self.tail = None
            self.lenght = 0
        else:
            # Новая голова - это prev предыдущей головы
            self.head = self.head.prev
            self.head.next = self.tail
            self.tail.prev = self.head
            self.lenght -= 1
        return data

    def popleft(self) -> object:
        if self.lenght == 0:
            return None

        data = self.tail.data
        if self.lenght == 1:
            self.head = None
            self.tail = None
            self.lenght = 0
        else:
            self.tail = self.tail.next
            self.tail.prev = self.head
            self.head.next = self.tail
            self.lenght -= 1
        return data    

    def remove(self, index: int) -> None:
        # Удаляет ячейку из списка по указанному индексу
        if index >= self.lenght or index < 0:
            raise IndexError('List index out of range')
        if index == 0:
            self.popleft()
            return None
        elif index == self.lenght - 1:
            self.pop()
            return None
        currentIndex = 0
        node = self.tail
        while currentIndex < index:
            node = node.next
            currentIndex += 1
        node.next.prev = node.prev
        node.prev.next = node.next
        del node
        return None        

    def count(self) -> int:
        return self.lenght

    def __str__(self):
        # Отображение списка, понятное человеку
        s = 'DLL: '
        if self.lenght == 0:
            return 'Empty DLL'

        node = self.tail
        while True:
            s += f'[{node.data}]'
            node = node.next
            if node == self.tail:
                break
            s += ' -> '
        return s    

    def __iter__(self):
        # Переопределение метода итерирования
        if self.lenght == 0:
            return None
        node = self.tail
        while True:
            yield node
            node = node.next
            if node is self.tail:
                break    

    def __getitem__(self, index):
        # Получить значение ячейки по индексу 
        # Работает и по обратному счёту (-1, -2 ...)
        if index < 0:
            if index < -self.lenght:
                raise IndexError('List index out of range')   
            node = self.head
            currentIndex = -1
            while currentIndex > index:
                node = node.prev
                currentIndex -= 1
            return node.data
        else:
            if index >= self.lenght:
                raise IndexError('List index out of range')
            node = self.tail
            currentIndex = 0
            while currentIndex < index:
                node = node.next
                currentIndex += 1
            return node.data                         

    def __setitem__(self, index, value):
        if index < 0:
            index = self.lenght + index
        if index >= self.lenght or index < 0:
            raise IndexError('List index out of range')    
        currentIndex = 0
        node = self.tail
        while currentIndex < index:
            node = node.next
            currentIndex += 1
        node.data = value
        return None


DLL = DoubleLinkedList()
DLL.append((43,53,6))
DLL.append({'10': 1, '20': 2})
DLL.appendleft('jij')
DLL.appendleft(10)
DLL.insert('abc', 4)
DLL[4] = 'cba'
print(DLL)

print(f'DLL find cba: ', DLL.index('cba'))
print(f'DLL count: {DLL.count()}')
print(f'DLL[-1]: {DLL[-1]}')

DLL.remove(4)
print('DLL removed index 4')
print(DLL)
print(f'DLL pop: {DLL.pop()}')
print(f'DLL pop: {DLL.pop()}')
print(f'DLL popleft: {DLL.popleft()}')
print(f'DLL popleft: {DLL.popleft()}')

print(f'DLL count: {DLL.count()}')

'''
Output:

DLL: [10] -> [jij] -> [(43, 53, 6)] -> [{'10': 1, '20': 2}] -> [cba]
DLL find cba:  4
DLL count: 5
DLL[-1]: cba
DLL removed index 4
DLL: [10] -> [jij] -> [(43, 53, 6)] -> [{'10': 1, '20': 2}]
DLL pop: {'10': 1, '20': 2}
DLL pop: (43, 53, 6)
DLL popleft: 10
DLL popleft: jij
DLL count: 0
'''