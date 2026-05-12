from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self, level=0):
        result = " " * level + self.data + "\n"
        if self.leftChild:
            result += self.leftChild.__str__(level+1)

        if self.rightChild:
            result += self.rightChild.__str__(level+1)

        return result


def preOrderTraversal(root):
    if not root:
        return
    print(root.data)
    preOrderTraversal(root.leftChild)
    preOrderTraversal(root.rightChild)

def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.leftChild)
    print(root.data)
    inOrderTraversal(root.rightChild)

def postOrderTraversal(root):
    if not root:
        return
    postOrderTraversal(root.leftChild)
    postOrderTraversal(root.rightChild)
    print(root.data)

def levelOrderTraversal(root):
    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")
        if current.leftChild:
            queue.append(current.leftChild)
        if current.rightChild:
            queue.append(current.rightChild)


def searchNode(root, target):
    if not root:
        return "Node not found"
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.data == target:
            return f"found node {target}"

        if current.leftChild:
            queue.append(current.leftChild)
        if current.rightChild:
            queue.append(current.rightChild)

    return "Node not found"

def insertNode(root, newNode):
    if not root:
        return newNode
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if not current.leftChild:
            current.leftChild = newNode
            return root
        else:
            queue.append(current.leftChild)

        if not current.rightChild:
            current.rightChild = newNode
            return root
        else:
            queue.append(current.rightChild)


newBT = TreeNode("Kubernetes")
cp = TreeNode("ControlPlane")
wn = TreeNode("WorkerNodes")
newBT.leftChild = cp
newBT.rightChild = wn
newNode1 = TreeNode("controlplane-1")
newNode2 = TreeNode("controlplane-2")
newNode3 = TreeNode("workernode-1")
newNode4 = TreeNode("workernode-2")
cp.leftChild = newNode1
cp.rightChild = newNode2
wn.leftChild = newNode3
wn.rightChild = newNode4
# print(newBT)
# postOrderTraversal(newBT)
# levelOrderTraversal(newBT)
# print(searchNode(newBT, "workernode-1"))
newNode5 = TreeNode("controlplane-3")
print(insertNode(newBT, newNode=newNode5))




