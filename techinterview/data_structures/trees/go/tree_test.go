package main

import "testing"

func TestTreeIsEmpty(t *testing.T) {
    tree := NewTree()
    if tree.Root != nil {
        t.Errorf("Tree was not initialized with a nil root")
    }
}

func TestFirstInsertBecomesRoot(t *testing.T) {
    tree := NewTree()
    expected := 42
    tree.Insert(expected)
    got := tree.Root.Value
    if got != expected {
        t.Errorf("Expected: ", expected, "got", got)
    }
}

func TestInsertTwoFirstIsRootSecondIsChild(t *testing.T) {
    tree := NewTree()
    expected := []int{42, 20}

    for _, v := range expected {
        tree.Insert(v)
    }

    if tree.Root.Value != expected[0] {
        t.Errorf("Expected root to be", expected[0], "got", tree.Root.Value)
    }
    if tree.Root.Left.Value != expected[1] {
        t.Errorf("Expected root to be", expected[1], "got", tree.Root.Left.Value)
    }
}

func TestAddLotsOfNodesAndTheyEndUpInCorrectSpots(t *testing.T) {
    tree := NewTree()
    tree.Insert(50)
    tree.Insert(30)
    tree.Insert(20)
    tree.Insert(40)
    tree.Insert(70)
    tree.Insert(60)
    tree.Insert(80)

    if tree.Root.Value != 50 {
        t.Errorf("Expected", 50, "got", tree.Root.Value)
    }
    if tree.Root.Left.Value != 30 {
        t.Errorf("Expected", 30, "got", tree.Root.Left.Value)
    }
    if tree.Root.Left.Left.Value != 20 {
        t.Errorf("Expected", 20, "got", tree.Root.Left.Left.Value)
    }
    if tree.Root.Left.Right.Value != 40 {
        t.Errorf("Expected", 40, "got", tree.Root.Left.Right.Value)
    }
    if tree.Root.Right.Value != 70 {
        t.Errorf("Expected", 70, "got", tree.Root.Right.Value)
    }
    if tree.Root.Right.Left.Value != 60 {
        t.Errorf("Expected", 60, "got", tree.Root.Right.Left.Value)
    }
    if tree.Root.Right.Right.Value != 80 {
        t.Errorf("Expected", 80, "got", tree.Root.Right.Right.Value)
    }

}
