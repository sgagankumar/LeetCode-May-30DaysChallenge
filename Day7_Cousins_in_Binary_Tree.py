# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depth=0
        parent=0
        nodex=None
        nodey=None
        # print('root\tdepth\tparent')
        tree = self.traverse(root,depth,parent)
        # print(tree)
        for node in tree:
            # print(node)
            if(node[0]==x):
                nodex=(node[1],node[2])
            if(node[0]==y):
                nodey=(node[1],node[2])
        # print('n1:',nodex)
        # print('n2:',nodey)
        if(nodex[0]==nodey[0]):
            if(nodex[1]!=nodey[1]):
                return True
            else:
                return False
        else:
            return False

            
        
    def traverse(self, root, depth, parent):
        subtree = list()
        subtree.append([root.val,depth,parent])
        # print(root.val,',\t',depth,',\t',parent)
        parent=root.val
        depth+=1
        if(root.left != None):
            subtree1 = self.traverse(root.left, depth, parent)
            subtree+=subtree1
        if(root.right !=None):
            subtree2 = self.traverse(root.right, depth, parent)
            subtree+=subtree2
        return subtree  