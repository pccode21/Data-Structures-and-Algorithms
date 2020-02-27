class Node(object):
    def __init__(self, key, value, left=None, right=None):
        self.key = key  # 存储索引数值
        self.value = value  # 存储具体的数
        self.left = left  # 左节点
        self.right = right  # 右节点
        self.is_delete = False  # 删除标记, True为被删除,不会被搜索到
        self.bf = 0  # 平衡差,为左子树层级减去右子树层级，介于[-1,1]为合法值


class BalancedBinaryTree(object):
    """
    最小不平衡树 距离插入节点处最近的一个bf为-1/1的节点,
    新插入的节点若插入后引起树的不平衡,只要更改此节点为平衡树,则整个树就会平衡
    """

    def __init__(self):
        self.root = None

    @staticmethod
    def left_whirl(node):
        """
        左旋
        当node值为-2的时候可以执行此操作使其节点值为0,node为最小不平衡树的根节点
        :param node:
        :return:
        """
        node.bf = node.right.bf = 0

        node_right = node.right
        node.right = node.right.left
        node_right.left = node
        return node_right

    @staticmethod
    def right_whirl(node):
        """
        右旋
        当node值为2的时候可以执行此操作使其节点值为0,node为最小不平衡树的根节点
        :param node:
        :return:
        """
        node.bf = node.left.bf = 0

        node_left = node.left
        node.left = node.left.right
        node_left.right = node
        return node_left

    @staticmethod
    def left_right_whirl(node):
        """
        左右旋,先左旋子节点,再右旋node节点
        :param node:
        :return:
        """
        node_b = node.left
        node_c = node_b.right
        node.left = node_c.right
        node_b.right = node_c.left
        node_c.left = node_b

        node_c.right = node

        if node_c.bf == 0:
            node.bf = node_b.bf = 0
        elif node_c.bf == 1:
            node.bf = -1
            node_b.bf = 0
        else:
            node.bf = 0
            node_b.bf = 1

        node_c.bf = 0
        return node_c

    @staticmethod
    def right_left_whirl(node):
        """
        右左旋,先右旋子节点,再左旋node节点
        :param node:
        :return:
        """
        node_b = node.right
        node_c = node_b.left

        node_b.left = node_c.right
        node.right = node_c.left
        node_c.right = node_b

        node_c.left = node

        if node_c.bf == 0:
            node.bf = node_b.bf = 0
        elif node_c.bf == 1:
            node.bf = 0
            node_b.bf = -1
        else:
            node.bf = 1
            node_b.bf = 0

        node_c.bf = 0
        return node_c

    def insert(self, key, value):
        """
        插入数据
        1 寻找插入点,并记录下距离该插入点的最小非平衡子树及其父子树
        2 修改最小非平衡子树到插入点的bf
        3 进行调整
        :param key:
        :param value:
        :return:
        """

        if not self.root:
            self.root = Node(key, value)
            return

        # a:最小非平衡树节点 p:插入点
        a, p = self.root, self.root

        # a与p节点的父节点,a_father用以链接旋转后的节点, p_father用以在循环时给a_father赋值
        a_father, p_father = None, None

        # 寻找插入点,并记录下距离该插入点的最小非平衡子树(a) 父子树(a_father) 插入点(p)
        while p:
            if p.key == key:
                # 直接修改
                p.value = value
                return

            if p.bf != 0:
                a_father, a = p_father, p

            p_father = p
            if key > p.key:
                p = p.right
            else:
                p = p.left

        # 插入点
        node = Node(key, value)

        if key > p_father.key:
            p_father.right = node
        else:
            p_father.left = node

        # 修改从a到插入点p的bf值
        ta = a
        while ta:
            if ta.key == key:
                break
            elif key > ta.key:
                ta.bf -= 1
                ta = ta.right
            else:
                ta.bf += 1
                ta = ta.left

        # 判断新节点是插入在a子节点的左边(True)还是右边(False)
        if a.key > key:
            p_pos = a.left.key > key
        else:
            p_pos = a.right.key > key

        # 旋转修改
        if a.bf > 1:
            # 新节点插入到了a节点的左边并导致了不平衡,此时需要判断是要进行右旋转还是左右旋转
            if p_pos:
                a = BalancedBinaryTree.right_whirl(a)
            else:
                a = BalancedBinaryTree.left_right_whirl(a)
        elif a.bf < -1:
            # 新节点插入到了a节点的右边并导致了不平衡,此时需要判断是要进行左旋转还是右左旋转
            if p_pos:
                a = BalancedBinaryTree.right_left_whirl(a)
            else:
                a = BalancedBinaryTree.left_whirl(a)

        # 将调整后的a节点加入到a_father节点中
        if a_father:
            if a_father.key > key:
                a_father.left = a
            else:
                a_father.right = a
        else:
            self.root = a

    def delete(self, key):
        """
        删除节点并返回该节点的值
        :return:
        """
        p = self._search(key)
        if not p:
            return False

        p.is_delete = True
        return True

    def pop(self, key):
        p = self._search(key)
        if not p:
            return None

        p.is_delete = True
        return p.value

    def _search(self, key):
        p = self.root
        while p:
            if p.key == key:
                if p.is_delete:
                    p = None
                break
            elif p.key > key:
                p = p.left
            else:
                p = p.right
        else:
            return None

        return p

    def search(self, key):
        res = self._search(key)
        if res:
            return res.value

        return None


if __name__ == "__main__":
    a = [(1, 'a'), (2, 'g'), (3, 'h'), (4, 'b'), (5, 'd'), (3.5, 'e')]
    bbt = BalancedBinaryTree()
    for item in a:
        bbt.insert(item[0], item[1])
    print(bbt.search(1), bbt.pop(1), bbt.search(1))
