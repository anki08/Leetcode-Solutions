def goodNodes(self, root) -> int:
    if root is None:
        return 0

    return 1 + self.goodnodesUtil(root.left, root.val) + self.goodnodesUtil(root.right, root.val)


def goodnodesUtil(self, root, max_val):
    if root is None:
        return 0

    res = 0
    if (root.val >= max_val):
        print(root.val)
        print(max_val)
        max_val = root.val
        res = 1

    # res += self.goodnodesUtil(root.left, max_val)
    res += self.goodnodesUtil(root.right, max_val)
    return res
