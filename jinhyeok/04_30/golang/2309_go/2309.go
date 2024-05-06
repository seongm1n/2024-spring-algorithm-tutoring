package golang

import (
	"fmt"
	"sort"
)

func main() {
	// 아홉 난쟁이의 키를 저장할 슬라이스 생성
	heights := make([]int, 9)

	// 표준 입력으로부터 아홉 난쟁이의 키를 읽어옴
	for i := 0; i < 9; i++ {
		fmt.Scan(&heights[i])
	}

	// 아홉 난쟁이 중 두 명을 선택하는 모든 조합을 구하기 위한 이중 반복문
	for i := 0; i < 8; i++ {
		for j := i + 1; j < 9; j++ {
			sum := 0
			// 아홉 난쟁이 키의 총합 계산
			for _, height := range heights {
				sum += height
			}

			// 선택된 두 명의 키를 제외한 일곱 난쟁이의 키의 합이 100인 경우
			if sum-heights[i]-heights[j] == 100 {
				// 선택된 두 명을 제외한 일곱 난쟁이 선택
				result := make([]int, 0)
				for k := 0; k < 9; k++ {
					if k != i && k != j {
						result = append(result, heights[k])
					}
				}
				// 선택된 일곱 난쟁이의 키를 오름차순으로 정렬
				sort.Ints(result)
				// 선택된 일곱 난쟁이의 키를 출력
				for _, height := range result {
					fmt.Println(height)
				}
				return
			}
		}
	}
}
