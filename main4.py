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

    def deleteSubtreeNode(self, node):
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

    def deleteNode(self, node):
        if node is None:
            return None
        if not node.hasLeftChild() or not node.hasRightChild():
            removed_node = node
        else:
            removed_node = node.rightChild
            while removed_node.hasLeftChild(): removed_node = removed_node.leftChild
        if removed_node.hasLeftChild():
            node_to_replace = removed_node.leftChild
        else:
            node_to_replace = removed_node.rightChild
        if node_to_replace is not None:
            node_to_replace.parent = removed_node.parent
        if removed_node.parent is not None:
            if removed_node is removed_node.parent.leftChild:
                removed_node.parent.leftChild = node_to_replace
            else:
                removed_node.parent.rightChild = node_to_replace
        else:
            self.root = node_to_replace
        if removed_node is not node:
            node.value = removed_node.value
        del removed_node    



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
    tree.deleteSubtreeNode(node)
    tree.showTree()
    node, message = tree.find(50)
    print(message)
    tree.deleteNode(node)
    tree.pasteValue(50)
    _, message = tree.find(50)
    print(message)
    tree.showTree()


''' Output
    Empty Tree
Already exists!
50
| - 30
| - | - 15
| - | - | - 0
| - | - | - | - 5
| - | - | - | - | - 10
| - | - | - 20
| - | - | - | - 25
| - | - 40
| - | - | - 35
| - | - | - 45
| - 100
| - | - 75
| - | - | - 60
| - | - | - | - 55
| - | - | - | - 65
| - | - | - | - | - 70
| - | - | - 95
| - | - | - | - 90
| - | - | - | - | - 85
| - | - | - | - | - | - 80
Not found
50 -> 100 -> 75 (found 75)
(deleted 75)
50
| - 30
| - | - 15
| - | - | - 0
| - | - | - | - 5
| - | - | - | - | - 10
| - | - | - 20
| - | - | - | - 25
| - | - 40
| - | - | - 35
| - | - | - 45
| - 100
50 (found 50)
(deleted 50)
(added 50)
100 -> 30 -> 40 -> 45 -> 50 (found 50)
100
| - 30
| - | - 15
| - | - | - 0
| - | - | - | - 5
| - | - | - | - | - 10
| - | - | - 20
| - | - | - | - 25
| - | - 40
| - | - | - 35
| - | - | - 45
| - | - | - | - 50
'''    
