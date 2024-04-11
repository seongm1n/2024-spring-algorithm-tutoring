#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, l;
int tmp;
vector<int> v;

int main(void)
{
    cin >> n >> l;

    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        v.push_back(tmp);
    }

    sort(v.begin(), v.end());

    for (int i = 0; i < n; i++)
    {
        if (v[i] <= l)
        {
            l++;
        }
        else
        {
            break;
        }
    }

    cout << l << endl;
    return 0;
}
