#include <iostream>

using namespace std;

#define MAX_MONEY 1000

// 잔돈 리스트
int money_list[6] = {500, 100, 50, 10, 5, 1};

// 거슬러주는 동전의 갯수.
int coin_num = 0;

int main() {

  // 1000엔의 지페를 한 장 받기 때문에 입력값은 이보다 클 수 없음.
  int money = 0;
  cin >> money;

  if (money > 1000 || money < 0) {
    printf("Money는 1000보다 클 수 없습니다. \n");
    return 0;
  }

  money = 1000 - money;

  for (int i = 0; i < 6; i++) {
    coin_num += money / money_list[i];
    money = money % money_list[i];
  }

  cout << coin_num << endl;

  return 0;
}