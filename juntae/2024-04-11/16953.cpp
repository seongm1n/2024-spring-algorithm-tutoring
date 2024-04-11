#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

long long int n, m;

int bfs(int i)
{
    queue<pair<long long int, long long int>> q;
    q.push({i, 0});

    while (!q.empty())
    {
        long long int x = q.front().first;
        long long int cnt = q.front().second;
        q.pop();

        if (x == m)
        {
            return cnt + 1;
        }

        if (x * 2 <= m)
        {
            q.push({x * 2, cnt + 1});
        }

        if ((x * 10) + 1 <= m)
        {
            q.push({(x * 10) + 1, cnt + 1});
        }
    }
    return -1;
}

int main(void)
{
    cin >> n >> m;
    int result = bfs(n);
    cout << result << endl;
    return 0;
}
