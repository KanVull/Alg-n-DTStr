class Node:
    def __init__(self, data: any) -> None:
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

    def append(self, value: any) -> None:
        node = Node(value)
        if self.head:
            self.tail.prev = node
            self.head.next = node
            node.next = self.tail
            node.prev = self.head
            self.head = node
            
        else:
            self.head = node
            self.tail = node
            self.head.next = node
            self.head.prev = node
            self.tail.next = node
            self.tail.prev = node   

        self.lenght += 1

    def __str__(self) -> str:
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
        node = self.tail
        while True:
            yield node
            node = node.next
            if node is self.tail:
                break    
           

DLL = DoubleLinkedList()
DLL.append((43,53,6))
DLL.append({'10': 1, '20': 2})
DLL.append('jija')
DLL.append(4)
print(DLL)
for node in DLL:
    print(node)