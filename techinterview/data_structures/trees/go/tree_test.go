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
