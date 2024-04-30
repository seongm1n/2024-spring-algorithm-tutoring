#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  int N,L; // 과일의 수와 스네이크버드의 초기 길이.
  std::cin >> N >> L;

  std::vector<int> heights(N); // 과일들의 높이를 저장할 벡터.
  for (int i = 0; i < N; i++) {
    std::cin >> heights[i];
  }

  // 과일들의 높이를 오름차순으로 정렬.
  std::sort(heights.begin(), heights.end());

  // 정렬된 과일을 순회하면서 스네이크버드의 길이 증가.
  for (int height : heights) {
    if (height <= L) {
      L += 1; // 현재 길이가 과일의 높이 이하이면 과일을 먹고 길이 증가.
    }
    else {
      break; // 더 이상 먹을 수 있는 과일이 없으므로 종료.
    }
  }

  std::cout << L << std::endl;

  return 0;
}