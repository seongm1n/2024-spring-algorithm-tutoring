#include <iostream>
using namespace std;

int money[6] = {500, 100, 50, 10, 5, 1};
int cnt = 0;

int main(void)
{
    int n;
    cin >> n;
    n = 1000 - n;

    for (int i = 0; i < 6; i++)
    {
        cnt += n / money[i];
        n = n % money[i];
    }

    cout << cnt << endl;
    return 0;
}
