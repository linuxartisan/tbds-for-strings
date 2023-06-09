from TBDSNode import TBDSNode

class TBDS:
    def __init__(self):
        self.root = TBDSNode()

    # Adds the key-value pair to the TBDS
    def add(self, key: str, value : str) -> None:
        if key == '' or key is None:
            return
        self._add(self.root, key, value)

    # Helper method to add
    def _add(self, currentNode: TBDSNode, currentKey: str, value: str) -> None:
        # Reached the node that matches with the actual key;
        # so update the value
        if currentKey == '':
            currentNode.value = value
            # print("Modified node:", value)
            return

        children = currentNode.children
        firstChar = currentKey[0] # first character of the current key

        if firstChar in children:
            # The node with character firstChar is already present, go one level deep
            presentNode = children[firstChar]
            self._add(presentNode, currentKey[1:], value)
        else:
            # The node with character firstChar is not present, create a new one
            newNode = TBDSNode()
            children[firstChar] = newNode
            self._add(newNode, currentKey[1:], value)



    # Returns the object value associated with the given key
    # If the key is not present in the TBDS, returns None
    def get(self, key: str) -> str:
        if key == '' or key is None:
            return None
        return self._get(self.root, key)

    def _get(self, currentNode: TBDSNode, currentKey: str) -> str:
        # Reached the final leaf node, and it matches the actual key;
        # so return value
        if currentKey == '':
            return currentNode.value
        
        children = currentNode.children
        firstChar = currentKey[0]

        if firstChar in children:
            # The node with character firstChar is already present, go one level deep
            presentNode = children[firstChar]
            return self._get(presentNode, currentKey[1:])

        # key not present, hence return None
        return None


    # Returns True if key is in the TBDS, False otherwise
    def containsKey(self, key: str) -> bool:
        if key == '' or key is None:
            return None
        return self._containsKey(self.root, key)

    def _containsKey(self, currentNode: TBDSNode, currentKey: str) -> bool:
        # Reached the final leaf node, and it matches the actual key.
        if currentKey == '':
            # Also, the leaf node contains a value, so return true
            return bool(currentNode.value)
        
        children = currentNode.children
        firstChar = currentKey[0]

        if firstChar in children:
            # The node with character firstChar is already present, go one level deep
            presentNode = children[firstChar]
            return self._containsKey(presentNode, currentKey[1:])

        return False


    # Returns a list of objects containing all keys that start with prefix
    def getKeysForPrefix(self, prefix: str) -> list:
        if prefix == '' or prefix is None:
            return []

        currentNode = self._findNode(self.root, prefix)
        if currentNode is None:
            return []

        return self._getSubtreeKeys(currentNode)

    # Recursive helper function to find node that matches a prefix
    def _findNode(self, currentNode: TBDSNode, prefix: str) -> TBDSNode:
        #
        if prefix == '':
            return currentNode

        children = currentNode.children
        firstChar = prefix[0]

        if firstChar in children:
            presentNode = children[firstChar]
            return self._findNode(presentNode, prefix[1:])
        
        return None

    # Recursive helper function to get all keys in a node's subtree
    def _getSubtreeKeys(self, currentNode: TBDSNode) -> list:
        keys = [] # list of keys

        # Add the value of current node to the list
        if currentNode.value:
            keys.append(currentNode.value)

        children = currentNode.children
        # if no children, then return keys
        if not children:
            return keys
        
        # get keys from subtree
        for elem in children:
            keys.extend(self._getSubtreeKeys(children[elem]))

        return keys


    # Prints all values stored inside the TBDS
    def print(self) -> None:
        print("The values in the tree:")
        self._print(self.root)

    # Helper method to print
    def _print(self, currentNode: TBDSNode) -> None:
        children = currentNode.children

        # if no children, then return
        if not children:
            return
        
        # iterate over the entries
        for key in children:
            presentNode = children[key]
            if presentNode.value:
                print(presentNode.value, sep='\t')
            self._print(presentNode)


    # Counts number of values stored in the TBDS
    def count(self) -> int:
        if not self.root:
            return 0

        return self._count(self.root)

    def _count(self, currentNode: TBDSNode) -> int:
        count = 0
        if currentNode.value:
            count += 1

        children = currentNode.children
        if not children:
            return count
        
        for elem in children:
            presentNode = children[elem]
            count += self._count(presentNode)

        return count
