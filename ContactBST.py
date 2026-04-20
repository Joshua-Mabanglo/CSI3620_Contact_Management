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
            print(f"{node.contact.name} | {node.contact.phone} | {node.contact.email}")
            self._inorder(node.right)
            
    def search(self, name):
        return self._search(self.root, name)
    
    def delete(self, name):
        self.root = self._delete(self.root, name)
    
    def _search(self, node, name):
        if node is None:
            return None
        
        # match found
        if name.lower() == node.contact.name.lower():
            return node.contact
        
        # go left
        if name.lower() < node.contact.name.lower():
            return self._search(node.left, name)
        
        # go right
        return self._search(node.right, name)
    
    def _delete(self, node, name):
        if node is None:
            return None
        
        # go left
        if name.lower() < node.contact.name.lower():
            node.left = self._delete(node.left, name)
            
        # go right
        elif name.lower() > node.contact.name.lower():
            node.right = self._delete(node.right, name)
            
        # found node
        else:
            # Case 1: no children
            if node.left is None and node.right is None:
                return None

            # Case 2: one child (right only)
            if node.left is None:
                return node.right

            # Case 2: one child (left only)
            if node.right is None:
                return node.left

            # Case 3: two children
            successor = self._min_value_node(node.right)
            node.contact = successor.contact
            node.right = self._delete(node.right, successor.contact.name)

        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current 