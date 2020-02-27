"""
二叉查找树（Binary Search Tree），又称为二叉搜索树、二叉排序树。其或者是一棵空树；或者是具有以下性质的二叉树：
若左子树不空，则左子树上所有结点的值均小于或等于它的根结点的值
若右子树不空，则右子树上所有结点的值均大于或等于它的根结点的值
左、右子树也分别为二叉排序树
https://blog.csdn.net/u010089444/article/details/70854510
"""


class Node:  # 定义树的结点类
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:  # 定义二叉查找树类
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    # 搜索
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    # 插入
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    # 删除
    def delete(self, root, data):
        flag, n, p = self.search(root, root, data)
        if flag is False:
            print("无该关键字，删除失败")
        else:
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                del p
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del p
            else:  # 左右子树均不为空
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del p

    """
    先序遍历
    访问顺序如下：
    访问根节点
    先序遍历左子树
    先序遍历右子树
    """

    def preOrderTraverse(self, node):
        if node is not None:
            print(node.data)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    """
    中序遍历
    访问顺序如下：
    中序遍历左子树
    访问根节点
    中序遍历右子树
    """

    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print(node.data)
            self.inOrderTraverse(node.rchild)

    """
    后序遍历
    访问顺序如下：
    后序遍历左子树
    后序遍历右子树
    访问根节点
    """

    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print(node.data)


a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
bst = BST(a)  # 创建二叉查找树
bst.inOrderTraverse(bst.root)  # 中序遍历
bst.delete(bst.root, 49)  # 删除数字 49
bst.inOrderTraverse(bst.root)  # 重新中序遍历
