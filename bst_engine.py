class BSTNode:

    def __init__(self, key, product):

        self.key = key
        self.product = product

        self.left = None
        self.right = None


class BSTEngine:

    def __init__(self):

        self.root = None


    def insert(self, key, product):

        self.root = self._insert(
            self.root,
            key,
            product
        )


    def _insert(self, node, key, product):

        if node is None:

            return BSTNode(key, product)

        if key < node.key:

            node.left = self._insert(
                node.left,
                key,
                product
            )

        else:

            node.right = self._insert(
                node.right,
                key,
                product
            )

        return node


    def inorder_traversal(self):

        result = []

        self._inorder(
            self.root,
            result
        )

        return result


    def _inorder(self, node, result):

        if node:

            self._inorder(
                node.left,
                result
            )

            result.append(node.key)

            self._inorder(
                node.right,
                result
            )
    def search(self, key):

        return self._search(

            self.root,

            key
        )


    def _search(

        self,

        node,

        key
    ):

        if node is None:

            return None

        if node.key == key:

            return node.product

        if key < node.key:

            return self._search(

                node.left,

                key
            )

        return self._search(

            node.right,

            key
        )      