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

    def deleteNode(self, node):
        if node is None:
            return None
        def _deleteNode(node):
            if node.hasLeftChild(): 
                _deleteNode(node.leftChild)
            if node.hasRightChild(): 
                _deleteNode(node.rightChild)
            del node

        if node.hasParent():
            parent = node.parent
            if parent.leftChild is node:
                parent.leftChild = None
            else:    
                parent.rightChild = None
            _deleteNode(node)
        else:
            _deleteNode(node)
            self.root = None 

    def find(self, value):
        curr_node = self.root
        if not curr_node:
            return None, 'Error! Empty Tree'
        while True:
            if value > curr_node.value:
                if curr_node.hasRightChild():
                    curr_node = curr_node.rightChild
                else:
                    return None, 'Not found'
            elif value < curr_node.value:
                if curr_node.hasLeftChild():
                    curr_node = curr_node.leftChild
                else:
                    return None, 'Not found'
            else:
                return curr_node, self._path(curr_node)                      
        
    def pasteValue(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:    
            curr_node = self.root
            while True:
                if value > curr_node.value:
                    if curr_node.hasRightChild():
                        curr_node = curr_node.rightChild
                    else:
                        node.parent = curr_node
                        curr_node.rightChild = node 
                        break
                elif value < curr_node.value:
                    if curr_node.hasLeftChild():
                        curr_node = curr_node.leftChild
                    else:
                        node.parent = curr_node
                        curr_node.leftChild = node
                        break           
                else:
                    print('Already exists!')
                    break

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
 

if __name__ == '__main__':
    import random as rnd
    tree = Tree()
    tree.showTree()
    tree.pasteValue(50)
    numbers = list(range(0,101,5))
    rnd.shuffle(numbers)
    for i in numbers:
        tree.pasteValue(i)
    tree.showTree()
    node, message = tree.find(6)
    print(message)
    node, message = tree.find(75)
    print(message)
    tree.deleteNode(node)
    tree.showTree()


''' Output
    Empty Tree
    Already exists!
    50
    | - 10
    | - | - 5
    | - | - | - 0
    | - | - 15
    | - | - | - 25
    | - | - | - | - 20
    | - | - | - | - 45
    | - | - | - | - | - 30
    | - | - | - | - | - | - 40
    | - | - | - | - | - | - | - 35
    | - 95
    | - | - 60
    | - | - | - 55
    | - | - | - 75
    | - | - | - | - 70
    | - | - | - | - | - 65
    | - | - | - | - 85
    | - | - | - | - | - 80
    | - | - | - | - | - 90
    | - | - 100
        (trying find 6)
    Not found 
        (success find 75)
    50 -> 95 -> 60 -> 75 
        (75 - deleted)
    50
    | - 10
    | - | - 5
    | - | - | - 0
    | - | - 15
    | - | - | - 25
    | - | - | - | - 20
    | - | - | - | - 45
    | - | - | - | - | - 30
    | - | - | - | - | - | - 40
    | - | - | - | - | - | - | - 35
    | - 95
    | - | - 60
    | - | - | - 55
    | - | - 100
'''    
