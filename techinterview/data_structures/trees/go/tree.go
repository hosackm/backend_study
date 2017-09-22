package main

import "fmt"

type Node struct {
    Right *Node
    Left *Node
    Value int
}

type Tree struct {
    Root *Node
}

// create a new node with no children and value set to value
func newNode(value int) *Node{
    return &Node{nil, nil, value}
}

// recursively search through subtrees to find location to insert new node
func (n *Node) insert(value int) {
    if value < n.Value {
        if n.Left == nil {
            n.Left = newNode(value)
        } else {
            n.Left.insert(value)
        }
    } else{
        if n.Right == nil {
            n.Right = newNode(value)
        } else {
            n.Right.insert(value)
        }
    }
}

// recursively traverse a tree in-order printing each node
func (n *Node) traverse() {
    if n != nil {
        n.Left.traverse()
        fmt.Printf("Node(%d)\n", n.Value)
        n.Right.traverse()
    }
}

// recursively traverses a tree search for a node that has the value. return true if it is found, false otherwise
func (n *Node) findValue(value int) bool {
    if n == nil {
        return false
    }
    if value == n.Value {
        return true
    }
    if value < n.Value {
        return n.Left.findValue(value)
    } else {
        return n.Right.findValue(value)
    }
}

// find the minimum node within a node's subtree
func (n *Node) findMinNodeInSubtree() *Node {
    if n.Left == nil {
        return n
    }
    return n.Left.findMinNodeInSubtree()
}

// recursively traverse a node's subtree and delete a node matching value
func (n *Node) delete(value int) *Node {
    if n == nil {
        return nil
    }
    if value < n.Value {
        n.Left = n.Left.delete(value)
    } else if value > n.Value {
        n.Right = n.Right.delete(value)
    } else {
        if n.Left == nil {
            return n.Right
        }
        if n.Right == nil {
            return n.Left
        }
        // two children, find the min and swap with this value
        minnode := n.Right.findMinNodeInSubtree()
        n.Value = minnode.Value
        n.Right = n.Right.delete(minnode.Value)
    }

    return n
}

// return a pointer to a new tree with no root
func NewTree() *Tree{
    return &Tree{nil}
}

// insert a node with value == value into a tree
func (t *Tree) Insert(value int) {
    if t.Root == nil{
        t.Root = newNode(value)
    } else {
        t.Root.insert(value)
    }
}

// searches for a node whose value is value and returns a bool indicating if it is present in the tree
func (t *Tree) Search(value int) bool {
    if t.Root == nil {
        return false
    }
    return t.Root.findValue(value)
}

func (t *Tree) Delete(value int) {
    if t.Root != nil {
        t.Root.delete(value)
    }
}

// traverse a tree in-order and print a node on each newline
func (t *Tree) Traverse() {
    fmt.Println("Tree:")
    t.Root.traverse()
}

func main() {
    t := NewTree()
    t.Insert(50);
    t.Insert(30);
    t.Insert(20);
    t.Insert(40);
    t.Insert(70);
    t.Insert(60);
    t.Insert(80);

    // tree:
    //         50
    //     30      70
    //  20   40  60   80


    // 20->30->40->50->60->70->80
    t.Traverse();

    t.Delete(20);
    // tree:
    //         50
    //     30      70
    //       40  60   80

    // 30->40->50->60->70->80
    t.Traverse();

    t.Delete(30);
    // tree:
    //         50
    //     40      70
    //           60   80

    // 40->50->60->70->80
    t.Traverse();

    t.Delete(50);
    // tree:
    //     60
    // 40      70
    //            80

    // 40->60->70->80
    t.Traverse();
}
