package golang

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// n, m 입력받기
		line := scanner.Text()
		parts := strings.Split(line, " ")
		n, _ := strconv.Atoi(parts[0])
		m, _ := strconv.Atoi(parts[1])

		if n == 0 && m == 0 {
			// 모두 0인 경우만 종료
			break
		}

		// 전화 통화 시작 시간과 끝 시간을 저장하는 슬라이스
		calls := make([][2]int, n)
		for i := 0; i < n; i++ {
			scanner.Scan()
			line := scanner.Text()
			parts := strings.Split(line, " ")
			start, _ := strconv.Atoi(parts[2])
			dur, _ := strconv.Atoi(parts[3])
			calls[i] = [2]int{start, start + dur}
		}

		// 각 구간의 결과를 저장할 슬라이스
		results := make([]int, m)
		for i := 0; i < m; i++ {
			scanner.Scan()
			line := scanner.Text()
			parts := strings.Split(line, " ")
			start, _ := strconv.Atoi(parts[0])
			dur, _ := strconv.Atoi(parts[1])
			end := start + dur

			// 구간에 포함되는 전화 통화의 수 계산
			count := 0
			for _, call := range calls {
				if min(end, call[1])-max(start, call[0]) >= 1 {
					count++
				}
			}
			results[i] = count
		}

		// 각 구간의 결과를 출력
		for _, result := range results {
			fmt.Println(result)
		}
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
