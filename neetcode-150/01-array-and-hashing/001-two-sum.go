package main

import "fmt"

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)

	for index, num := range nums {
		if value, found := m[target-num]; found {
			return []int{value, index}
		}

		m[num] = index
	}

	return nil
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSum([]int{3, 2, 4}, 6))
	fmt.Println(twoSum([]int{3, 3}, 6))
}
