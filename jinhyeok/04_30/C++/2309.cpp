#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> heights;

    // 아홉 난쟁이의 키를 입력받음.
    for (int i = 0; i < 9; i++) {
      int height;
      cin >> height;
      heights.push_back(height);
    }

    // 아홉 난쟁이 중 두 명을 선택하는 모든 조합을 구함.
    for (int i = 0; i < 8; i++) {
      for (int j = i + 1; j < 9; j++) {
        int sum = 0;
        for (int height : heights) {
          sum += height;
        }

        // 선택된 두 명의 키를 제외한 일곱 난쟁이의 키의 합이 100인 경우
        if (sum - heights[i] - heights[j] == 100) {
          vector<int> result;
          for (int k = 0; k < 9; k++) {
            if (k != i && k != j) {
              result.push_back(heights[k]);
            }
          }
          // 오름차순으로 정렬.
          sort(result.begin(), result.end());
          for (int height: result) {
            cout << height << endl;
          }
          return 0;
        }
      }
    }
    return 0;
}