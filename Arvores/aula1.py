from queue_1 import Queue

ROOT = "root"

class TreeNode:
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;

    def __str__(self):
        return str(self.data);

class BinaryTree:
    def __init__(self, data=None, node = None):
        if node:
            self.root = node
        elif data is None:
            self.root = None;
        else:   
            node = TreeNode(data)
            self.root = TreeNode(node);


    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)


        # print('')

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end='')
        # print('')

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright =  self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
    
    def levelorder_traversal(self, node = ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=' ')
        

class BinarySearchTree(BinaryTree):
    def insert(self, data):
        parent = None
        x = self.root
        while x:
            parent = x
            if data < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = TreeNode(data)
        elif data < parent.data:
            parent.left = TreeNode(data)
        else:
            parent.right = TreeNode(data)

    def search(self, value, node=0):
        if node == 0:
            node = self.root
        if node is None:
           return node 
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root;
        while node.left:
            node = node.left
        return node.data 
    
    def max (self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right;
        return node.data 
    
    def remove(self, value, node = ROOT):
        if node == ROOT:
            node = self.root
        if node == None:
            return node
        
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitue = self.min(node.right)
                node.data = substitue
                node.right = self.remove(substitue, node.right) 
        return node

# def postorder_example_tree():
#     tree = BinaryTree()
#     n1 = TreeNode('I')
#     n2 = TreeNode('N')
#     n3 = TreeNode('S')
#     n4 = TreeNode('C')
#     n5 = TreeNode('R')
#     n6 = TreeNode('E')
#     n7 = TreeNode('V')    
#     n8 = TreeNode('A')
#     n9 = TreeNode('5')
#     n10 = TreeNode('-')
#     n0 = TreeNode('3')

#     n0.left = n6
#     n0.right = n9
#     n6.left = n1
#     n6.right = n5
#     n5.left = n2
#     n5.right = n4
#     n4.right = n3
#     n9.left = n8
#     n9.right = n10
#     n8.right = n7

#     tree.root = n0
#     return tree


if __name__ == '__main__':
    tree = BinaryTree(10);
    tree.root.left = TreeNode(5);
    tree.root.right = TreeNode(15);
    print(tree.root.left);
    print(tree.root);
    print(tree.root.right);

    # n1 = TreeNode('a');
    # n2 = TreeNode('+');
    # n3 = TreeNode('*');
    # n4 = TreeNode('b');
    # n5 = TreeNode('-'); 
    # n6 = TreeNode('/');
    # n7 = TreeNode('c');
    # n8 = TreeNode('d');
    # n9 = TreeNode('e');

    # n6.left = n7;
    # n6.right = n8
    # n5.left = n6;
    # n5.right = n9;
    # n3.left = n4;
    # n3.right = n5;  
    # n2.left = n1;
    # n2.right = n3;

    # tree.root = n2;
    # tree.simetric_traversal(tree.root); 
    # print('')     
    # tree = postorder_example_tree()
    # print("Percurso em pós ordem:")
    # tree.postorder_traversal()

    # print(f"\nAltura da tree: {tree.height()}")