package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}

	checkedNode := make(map[*ListNode]bool)
	for head.Next != nil {
		checkedNode[head] = true
		if checkedNode[head.Next] {
			return true
		}
		head = head.Next
	}

	return false
}
