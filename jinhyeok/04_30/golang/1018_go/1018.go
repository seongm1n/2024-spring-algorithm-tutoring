package golang

import (
	"fmt"
)

func countDifferences(board []string, startRow, startCol int) int {
	count := 0
	for i := 0; i < 8; i++ {
		for j := 0; j < 8; j++ {
			// 홀수 칸은 'W'로, 짝수 칸은 'B'로 비교
			if (i+j)%2 == 0 {
				if board[startRow+i][startCol+j] != 'W' {
					count++
				}
			} else {
				if board[startRow+i][startCol+j] != 'B' {
					count++
				}
			}
		}
	}
	// 패턴을 반전시켰을 때의 개수와 비교하여 최소값 반환
	return min(count, 64-count)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)

	// 보드 정보를 저장할 슬라이스 생성
	board := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&board[i])
	}

	minDifferences := 64
	// 모든 가능한 시작 위치에 대해 체스판을 잘라내어 최소 차이 값을 찾음
	for i := 0; i <= n-8; i++ {
		for j := 0; j <= m-8; j++ {
			differences := countDifferences(board, i, j)
			minDifferences = min(minDifferences, differences)
		}
	}

	fmt.Println(minDifferences)
}
