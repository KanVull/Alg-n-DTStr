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
        self.cursor = None

    def __createList(self, node: Node) -> None:
        # Добавить первый элемент в список
        self.head = node
        self.tail = node
        self.cursor = node
        return None

    def appendRight(self, value: any) -> None:
        node = Node(value)
        if self.head:
            # Если список уже не пустой
            self.head.next = node
            node.prev = self.head
            self.head = node            
        else:
            self.__createList(node)  

        self.lenght += 1
        return None

    def appendLeft(self, value: any) -> None:
        node = Node(value)
        if self.tail:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node            
        else:
            self.__createList(node)  

        self.lenght += 1
        return None

    def moveCursorTo(self, value: any) -> None:
        # Перемещение курсора на ячейку со значением value
        if self.lenght == 0:
            raise Exception('Empty list, cursor is not defined')
        node = self.tail
        while True:
            if node.data == value:
                self.cursor = node
                return None
            node = node.next    
            if node is None:
                raise Exception('Item with value "value" is not founded')

    def find(self, value: any) -> any:
        # Поиск ячейки по значению
        # Перемещает курсор на найдённую ячейку
        # Если ячейка не была найдена, курсор не перемещается, функция возвращает None
        try:
            self.moveCursorTo(value)
        except Exception as e:
            return -1
        return self.cursor.data        

    def currentCursorData(self) -> any:
        if self.cursor:
            return self.cursor.data
        else:
            return None    

    def insertAfterCursor(self, value: any) -> None:
        # Вставляет новую ячейку в список после курсора
        if self.cursor is None:
            raise Exception('Empty list, cursor is not defined. Use append functions.')
        if self.cursor.next is None:
            self.appendRight(value)
            self.cursor.next = self.head
            return None

        node = Node(value)
        node.prev = self.cursor
        node.next = self.cursor.next
        self.cursor.next.prev = node
        self.cursor.next = node

        self.lenght += 1
        return None

    def popRight(self) -> object:
        if self.lenght == 0:
            # Нечего удалять, список пустой
            return None

        data = self.head.data
        if self.lenght == 1:
            # Затираем информацию о голове и хвосте списка
            self.head = None
            self.tail = None
            self.cursor = None
            self.lenght = 0
        else:
            if self.cursor.next is None:
                self.cursor = self.cursor.prev
                self.cursor.next = None
            self.head = self.head.prev
            self.head.next = None
            self.lenght -= 1
        return data

    def popLeft(self) -> object:
        if self.lenght == 0:
            return None

        data = self.tail.data
        if self.lenght == 1:
            self.head = None
            self.tail = None
            self.cursor = None
            self.lenght = 0
        else:
            if self.cursor.prev is None:
                self.cursor = self.cursor.next
            self.tail = self.cursor
            self.lenght -= 1
        return data    

    def removeCursorItem(self) -> None:
        # Передвигает курсор на ячейку после текущего курсора
        # Если курсор это последний жлемент в списке, то перемещает на элемент после
        # Если курсор это единственный элемент, происходит очистка списка

        if self.cursor is None:
            return None

        if self.cursor.prev is None:
            self.cursor = self.tail.next
            self.popLeft()
            return None
        elif self.cursor.next is None:
            self.cursor = self.head.prev
            self.popRight()
            return None

        node = self.cursor
        node.next.prev = node.prev
        node.prev.next = node.next
        self.cursor = node.next

        self.lenght -= 1
        del node
        return None        

    def count(self) -> int:
        return self.lenght

    def next(self) -> None:
        if self.cursor is None:
            raise Exception('Empty list, cursor is not defined')
        if self.cursor.next is None:
            raise Exception('Cursor over the range of the list')
        self.cursor = self.cursor.next
        return None

    def previous(self) -> None:
        if self.cursor is None:
            raise Exception('Empty list, cursor is not defined')
        if self.cursor.prev is None:
            raise Exception('Cursor over the range of the list')
        self.cursor = self.cursor.prev
        return None        

    def __str__(self):
        # Отображение списка, понятное человеку
        s = 'DLL: '
        if self.lenght == 0:
            return 'Empty DLL'

        node = self.tail
        while True:
            if self.cursor == node:
                s += 'cursor: '
            s += f'[{node.data}]'
            node = node.next
            if node is None:
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
            if node is None:
                break   

if __name__ == '__main__':

    DLL = DoubleLinkedList()
    DLL.appendLeft((43,53,6))
    DLL.appendLeft({'10': 1, '20': 2})
    DLL.appendRight('jij')
    DLL.appendRight(10)
    print(DLL)

    print(f'DLL find jij: ', DLL.find('jij'))
    print(f'DLL count: {DLL.count()}')

    print(DLL)
    DLL.next()
    print('Cursor moved next')
    print(DLL)
    DLL.previous()
    print('Cursor moved prev')
    print(DLL)
    DLL.previous()
    print('Cursor moved prev')
    print(DLL)
    DLL.insertAfterCursor(10000)
    print('10000 inserted after cursor')
    print(DLL)
    DLL.removeCursorItem()
    print('Cursor item removed')
    print(DLL)
    print(f'DLL popRight: {DLL.popRight()}')
    print(DLL)
    print(f'DLL popRight: {DLL.popRight()}')
    print(DLL)
    print(f'DLL popLeft: {DLL.popLeft()}')
    print(DLL)
    print(f'DLL popLeft: {DLL.popLeft()}')
    print(DLL)

    print(f'DLL count: {DLL.count()}')

    DLL.appendLeft((43,53,6))
    DLL.appendLeft({'10': 1, '20': 2})
    DLL.appendRight('jij')
    print(DLL)
    print('DLL cursor right now: ', DLL.currentCursorData())

    # iteration example
    for node in DLL:
        print(node)

'''
Output:

DLL: [{'10': 1, '20': 2}] -> cursor: [(43, 53, 6)] -> [jij] -> [10]

DLL find jij:  jij
DLL count: 4
DLL: [{'10': 1, '20': 2}] -> [(43, 53, 6)] -> cursor: [jij] -> [10]

Cursor moved next
DLL: [{'10': 1, '20': 2}] -> [(43, 53, 6)] -> [jij] -> cursor: [10]

Cursor moved prev
DLL: [{'10': 1, '20': 2}] -> [(43, 53, 6)] -> cursor: [jij] -> [10]

Cursor moved prev
DLL: [{'10': 1, '20': 2}] -> cursor: [(43, 53, 6)] -> [jij] -> [10]

10000 inserted after cursor
DLL: [{'10': 1, '20': 2}] -> cursor: [(43, 53, 6)] -> [10000] -> [jij] -> [10]
Cursor item removed
DLL: [{'10': 1, '20': 2}] -> cursor: [10000] -> [jij] -> [10]

DLL popRight: 10
DLL: [{'10': 1, '20': 2}] -> cursor: [10000] -> [jij]
DLL popRight: jij
DLL: [{'10': 1, '20': 2}] -> cursor: [10000]
DLL popLeft: {'10': 1, '20': 2}

DLL: cursor: [10000]
DLL popLeft: 10000
Empty DLL
DLL count: 0

DLL: [{'10': 1, '20': 2}] -> cursor: [(43, 53, 6)] -> [jij]
DLL cursor right now:  (43, 53, 6)

{'10': 1, '20': 2}
(43, 53, 6)
jij

'''