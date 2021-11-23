class Node():
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.leftChild = None
        self.rightChild = None

    def hasParent(self):
        return True if self.parent else False

    def hasLeftChild(self):
        return True if self.leftChild else False

    def hasRightChild(self):
        return True if self.rightChild else False         


class Tree():
    def __init__(self):
        self.root = None
        self.cursor = None

    def deleteNode(self):
        def _deleteNode(node):
            if node.hasLeftChild(): 
                _deleteNode(node.leftChild)
            if node.hasRightChild(): 
                _deleteNode(node.rightChild)
            del node

        if self.cursor.hasParent():
            parent = self.cursor.parent
            if parent.leftChild is self.cursor:
                parent.leftChild = None
            else:    
                parent.rightChild = None
            _deleteNode(self.cursor)
            self.cursor = parent
        else:
            _deleteNode(self.cursor)
            self.cursor = None    

    def find(self, value):
        ''' Рекурсивный поиск элемента '''
        def _find(node, value):
            if node.value == value:
                return node    
            answer = None             
            if node.hasLeftChild():
                answer = _find(node.leftChild, value)
            if node.hasRightChild():
                if answer is None:
                    answer = _find(node.rightChild, value)
            return answer        


        if not self.root:
            return 'Error! Empty Tree'
        node = self.root
        node = _find(node, value)
        if node:
            self.cursor = node
            return print(self._path(node))
        else:
            return print('Element not found')        
        
    def pasteValueUnderCursor(self, value, moveCursor=False):
        node = Node(value, parent=self.cursor)
        if self.cursor is None:
            self.root = node
            self.cursor = self.root
        else:    
            if not self.cursor.hasLeftChild():
                self.cursor.leftChild = node
                if moveCursor:
                    self.cursor = node
            elif not self.cursor.hasRightChild():
                self.cursor.rightChild = node
                if moveCursor:
                    self.cursor = node    
            else:
                print('Not available!')

    def moveCursorUp(self, show=False):
        if self.cursor is not None:
            if self.cursor.hasParent():
                self.cursor = self.cursor.parent
                if show:
                    print(self._path(self.cursor))
                return True
        return False

    def moveCursorDownLeft(self, show=False):
        if self.cursor is not None:
            if self.cursor.hasLeftChild():
                self.cursor = self.cursor.leftChild
                if show:
                    print(self._path(self.cursor))
                return True
        return False

    def moveCursorDownRight(self, show=False):
        if self.cursor is not None:
            if self.cursor.hasRightChild():
                self.cursor = self.cursor.rightChild
                if show:
                    print(self._path(self.cursor))
                return True
        return False    

    def showTree(self):
        def _showNode(node, level):
            s = level * '| - '
            s += str(node.value)
            print(s)
            if node.hasLeftChild():
                _showNode(node.leftChild, level+1)
            if node.hasRightChild():
                _showNode(node.rightChild, level+1)

        if self.root is not None:
            _showNode(self.root, 0)
        else:
            print('Empty Tree')                

    def _path(self, node):
        if node.hasParent():
            return self._path(node.parent) + ' -> ' + str(node.value)
        else:
            return str(node.value)    

    def showCursor(self):
        if self.cursor:
            print(self._path(self.cursor) + ' <cursor')
        else:
            print('Empty Tree') 

    def showCursorInfo(self):
        self.showCursor()
        if self.cursor:
            if self.cursor.hasLeftChild():
                print(f'  Left child: {self.cursor.leftChild.value}')
            else:
                print('  Left child: None')
            if self.cursor.hasRightChild():
                print(f'  Right child: {self.cursor.rightChild.value}')
            else:
                print('  Right child: None')          
            
                    


if __name__ == '__main__':
    tree = Tree()
    tree.showTree()
    tree.showCursorInfo()
    tree.pasteValueUnderCursor(1)
    tree.showCursorInfo()
    tree.pasteValueUnderCursor(2)
    tree.moveCursorUp()
    tree.pasteValueUnderCursor(3, True)
    tree.showTree()
    tree.showCursor()
    tree.pasteValueUnderCursor(4)
    tree.pasteValueUnderCursor(5)
    tree.moveCursorUp()
    tree.moveCursorDownLeft()
    tree.pasteValueUnderCursor(6)
    tree.pasteValueUnderCursor(7, True)
    tree.pasteValueUnderCursor(8)
    tree.pasteValueUnderCursor(9, True)
    tree.showTree()
    tree.showCursor()
    tree.find(6)
    tree.showCursorInfo()
    tree.find(7)
    tree.showCursorInfo()
    tree.deleteNode()
    tree.showTree()


''' Output
    Empty Tree
    Empty Tree
    1 <cursor
    Left child: None
    Right child: None
    1
    | - 2
    | - 3
    1 -> 3 <cursor
    1
    | - 2
    | - | - 6
    | - | - 7
    | - | - | - 8
    | - | - | - 9
    | - 3
    | - | - 4
    | - | - 5
    1 -> 2 -> 7 -> 9 <cursor
    1 -> 2 -> 6 (find)
    1 -> 2 -> 6 <cursor
        Left child: None
        Right child: None
    1 -> 2 -> 7 (find)
    1 -> 2 -> 7 <cursor
        Left child: 8
        Right child: 9
    1
    | - 2
    | - | - 6
    | - 3
    | - | - 4
    | - | - 5
    (deleted 7)
'''    
