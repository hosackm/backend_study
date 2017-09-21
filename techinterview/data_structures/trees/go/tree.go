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

// traverse a tree in-order and print a node on each newline
func (t *Tree) Traverse() {
    fmt.Println("Tree:")
    t.Root.traverse()
}
