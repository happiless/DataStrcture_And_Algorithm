#include <iostream>
using namespace std;

int main() {
    int n , m , num[105][105], t;
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
             cin >> num[i][j];
        }
    }
    cin >> t;
    int x = n, y = 1;
    while (x >= 1 && y <= m) {
        if (num[x][y] == t) {
            cout << x << " " << y << endl;
            return 0;
        }
        if (num[x][y] > t) {
            x--;
        } else {
            y++;
        }
    }
    cout<< -1 << endl;
    return 0;
}
