package main

import "testing"

func getInts() []int {
    return []int{5, 4, 9, 1, 2, 3, 10, 8, 7, 6}
}

func TestMissingIsNotFound(t *testing.T) {
    arr := getInts()
    for _, v := range []int{-1, 0, 11, 42} {
        if BinarySearch(arr, v) {
            t.Errorf("Binary Search found %d which isn't in the array", v)
        }
    }
}

func TestExistingIsFound(t *testing.T) {
    arr := getInts()
    for _, v := range []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} {
        if BinarySearch(arr, v) == false {
            t.Errorf("Binary Search couldn't find %d which is in the array", v)
        }
    }
}
