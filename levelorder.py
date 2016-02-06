__author__ = 'cue'
from collections import deque
class node (object):
    level = 0
    data = ''
    child = []
    def __init__(self,data):
        self.data = data
        self.child = []

    def add_child(self,ch):
        ch.level = self.level + 1
        self.child.append(ch)




def levelorder(root):
    temproot =root
    que = deque()
    currentlevel = 0
    while temproot is not None:
        if  currentlevel != temproot.level:
            currentlevel = temproot.level
            print ("")

        print (temproot.data, end='')

        countchild  = len(temproot.child)
        if countchild != 0:
            que.extend(temproot.child)
        if  len(que) == 0:
            break
        temproot = que.popleft()

def print_tree (root):
    print (root.data, "level",root.level)
    for chil in root.child:
        print_tree(chil)
if __name__ == '__main__':
    root = node('A')
    child1 = node('B')
    child2 = node('C')
    child3 = node('D')
    child3_1 = node('E')
    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)
    child3.add_child(child3_1)
    levelorder(root)
    #print_tree(root)



