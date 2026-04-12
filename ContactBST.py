from Contact import Contact

class BSTNode:
    def __init__(self, contact):
        self.contact = contact
        self.left = None
        self.right = None
        
class ContactBST:
    def __init__(self):
        self.root = None
        
    def insert(self, contact):
        if self.root is None:
            self.root = BSTNode(contact)
        else:
            self._insert(self.root, contact)
            
    def _insert(self, node, contact):
        if contact.name.lower() < node.contact.name.lower():
            if node.left is None:
                node.left = BSTNode(contact)
            else:
                self._insert(node.left, contact)
        else:
            if node.right is None:
                node.right = BSTNode(contact)
            else:
                self._insert(node.right, contact)
                
    def display_sorted(self):
        self._inorder(self.root)
        
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.contact.name, node.contact.phone, node.contact.email)
            self._inorder(node.right)