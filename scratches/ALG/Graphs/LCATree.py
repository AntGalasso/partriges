"""
    tree class and dfs


"""

class Tree:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def trovaPadre(self, root, valore_figlio):
        if root is None:
            return None
        for c in root.children:
            if c.value == valore_figlio:
                return root
        for c in root.children:
            result = self.trovaPadre(c, valore_figlio)
            if result is not None:
                return result

    def printNodo(self, root):
        print(root.value)

    def printAlbero(self, root, depth=0):
        if root is None:
            return
        print(' ' * depth * 2 + str(root.value))
        for c in root.children:
            self.printAlbero(c, depth + 1)

    def esploraDFS(self, root, explored = None):
        if explored is None:
            return { }
        if root is None:
            return explored
        explored[root.value] = True
        for c in self.children:
            if explored[c.value] is False:
                self.esploraDFS(c, explored)





def huffmannTree(frequences):
    # Step 1: Create leaves (Tree nodes) from the frequencies
    frequences = sorted([Tree(val) for val in frequences], key=lambda v: v.value)

    # Step 2: Build the Huffman Tree
    while len(frequences) > 1:  # Continue while there are at least two nodes to combine
        # Take the two nodes with the lowest frequency
        left = frequences.pop(0)
        right = frequences.pop(0)

        # Create a new node with the sum of frequencies as the value
        combined_value = left.value + right.value
        combined_node = Tree(combined_value, [left, right])

        # Insert the combined node back into the sorted list
        frequences.append(combined_node)
        frequences = sorted(frequences, key=lambda v: v.value)

    # The remaining node is the root of the Huffman tree
    return frequences[0]

leaf = Tree(5)

sub1 = Tree(3, [Tree(6), Tree(88)])
sub2 = Tree(4, [leaf])

t = Tree(1, [sub1, sub2])

t.printNodo(leaf)
t.printAlbero(t)
print("huffmannn")



"""q = [1, 3, 4, 5, 6, 7, 2]
root = huffmannTree(q)
root.printAlbero(root)
"""
