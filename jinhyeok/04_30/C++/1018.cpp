#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 주어진 시작 위치(startRow, startCol)에서 8x8 크기의 체스판을 잘라내었을 때, 체스판 패턴에 맞지 않는 정사각형의 개수를 계산.
int countDifference(const vector<string>& board, int startRow, int startColumn) {
  int count = 0; // 패턴에 맞지 않는 칸의 개수.
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      if ((i + j) % 2 == 0) { // 홀수 칸
        if (board[startRow + i][startColumn + j] != 'W') {
          count++;
        }
      } else { // 짝수 칸
        if (board[startRow + i][startColumn + j] != 'B') {
          count++;
        }
      }
    }
  }
  // 최종적으로 count와 64 - count 중 작은 값을 반환.
  // 이는 패턴을 반전시켰을 때의 개수를 고려하기 위함.
  return min(count, 64 - count);
}

int main() {
  int N, M;
  cin >> N >> M;

  vector<string> board(N);
  for (int i = 0; i < N; i++) {
    cin >> board[i];
  }

  int minDifferences = 64;
  // 이중 반복문을 사용하여 모든 가능한 시작 위치에 대해 countDifferences 함수를 호출하여 최소 차이 값을 찾음.
  // 시작 위치는 (0, 0) -> (N-8, M-8)까지 가능.
  for (int i = 0; i <= N - 8; i++) {
    for (int j = 0; j <= M - 8; j++) {
      int differences = countDifference(board, i, j);
      minDifferences = min(minDifferences, differences); // 현재까지 찾은 최소 차이 값 저장.
    }
  }

  cout << minDifferences << endl;

  return 0;
}

// 위 코드에서 시간 복잡도는 O(N*M)이며, 보드의 크기에 따라 모든 가능한 시작 위치에 대해 8x8 크기의 체스판을 확인함.
// 주어진 보드에서 가능한 모든 8x8 크기의 체스판을 확인하여 최소 차이 값을 찾는 것이 핵심.