#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n;
int sum = 0;
vector<int> v;

int main(void)
{
    for (int i = 0; i < 9; i++)
    {
        cin >> n;
        v.push_back(n);
        sum += n;
    }

    sort(v.begin(), v.end());

    for (int i = 0; i < 9; i++)
    {
        for (int j = 1; j < 9; j++)
        {
            if (sum - v[i] - v[j] == 100)
            {
                for (int k = 0; k < 9; k++)
                {
                    if (k != i && k != j)
                    {
                        cout << v[k] << "\n";
                    }
                }
                return 0;
            }
        }
    }
    return 0;
}
