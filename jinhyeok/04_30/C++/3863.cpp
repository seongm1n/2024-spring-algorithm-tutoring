#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  // ios_base::sync_with_stdio와 cin.tie(NULL)를 사용하여 입출력 속도를 향상시킴.
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, m;

  // n, m을 입력받고 두 변수가 0이 아닌 동안 반복.
  while (cin >> n >> m && n != 0 && m != 0) {
    // 전화 정보를 저장하는 벡터.
    vector<pair<long long, long long>> calls(n);

    // 각 전화 통화의 정보를 입력받고, calls 벡터에 시작 시간과 끝나는 시간을 저장.
    for (int i = 0; i < n; i++) {
      long long src, dest, start, dur;
      cin >> src >> dest >> start >> dur;
      calls[i] = make_pair(start, start + dur);
    }

    for (int i = 0; i < m; i++) {
      long long start, dur; // 구간의 시작 시간과 지속 시간.
      cin >> start >> dur;
      long long end = start + dur; // 구간의 끝나는 시간 계산.
      int count = 0; // 구간에 포함되는 전화 통화의 수를 저장할 변수를 초기화 시킴.
      for (const auto& call : calls) { // 각 전화에 대해 반복.
        long long cStart = call.first; // 전화 통화의 시작 시간.
        long long cEnd = call.second; // 전화 통화의 끝나는 시간.
        if (min(end, cEnd) - max(cStart, start) >= 1) { // 구간에 포함되는 전화 통화의 조건을 확인하고, 포함되는 경우 count++
          count++;
        }
      }
      cout << count << endl;
    }
  }
  return 0;
}