/*
이 문제는 정수 A에서 B로 변환하는 최소 연산 횟수를 찾는 것이다.
두 가지 연산만 허용되며, 연산은 다음과 같다.

1. 2를 곱한다
2. 수의 오른쪽 끝에 1을 추가한다.

여기서 효율적으로 생각하기 위해서 역방향으로 생각하는 것이 좋다.

B에서 시작하여 A를 만들어보는 방식이다.

1. B에서 출발하여, 가능한 연산을 거꾸로 적용하며 A를 향해 나아간다.
2. B의 마지막 숫자가 1이라면, 1을 제거(이는 역으로 생각할 때 2번에 해당한다.)
3. B가 짝수라면, 2로 나눈다 (이는 역으로 생각할 때 1번에 해당.)
*/

#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int A, B;

int solve(int A, int B) {
  queue<pair<int, int>> q;
  q.push({B, 1}); // 초기값 B와 연산 횟수 1을 큐에 삽입.

  while (!q.empty()) {
    int current = q.front().first;
    int count = q.front().second;
    q.pop();

    if (current == A) {
      return count;
    }

    if (current < A) {
      continue;
    }

    if (current % 2 == 0) { // 현재 값이 짝수일 때 2로 나눔.
      q.push({current / 2, count + 1});
    }

    if (current % 10 == 1) { // 현재 값의 마지막 숫자가 1이면 마지막 숫자를 제거한다.
      q.push({current / 10, count + 1});
    }
  }

  return -1; // A로의 변환이 불가능한 경우.
}

int main() {

  cin >> A >> B;
  cout << solve(A, B) << endl;
  return 0;
}