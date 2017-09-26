package main

import (
    "fmt"
    "sort"
)

func BinarySearch(array []int, value int) bool {
    // make a copy so we don't modify the array that is passed in
    tmp := make([]int, len(array))
    copy(tmp, array)
    sort.Ints(tmp)

    // define function so we can call it recursively inside the definition
    brec := func (a []int, value int) bool { return true }
    brec = func (a []int, value int) bool {
        if len(a) < 2 {
            return a[0] == value
        }

        mid := len(a) / 2
        if value < a[mid] {
            return brec(a[:mid], value)
        } else if value > a[mid] {
            return brec(a[mid:], value)
        } else {
            return true
        }
    }

    return brec(tmp, value)
}

func main() {
    a := []int{5, 3, 2, 4, 1}
    vals := []int{1, 6}

    for _, v := range(vals) {
        if BinarySearch(a, v) {
            fmt.Printf("%v is in the slice\n", v)
        } else {
            fmt.Printf("%v is not in the slice\n", v)
        }
    }
}
