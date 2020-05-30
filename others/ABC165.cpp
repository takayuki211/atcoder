// ABC165

#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

// A
int main(){
  int k, a, b;
  cin >>k >> a >> b;
  if (a <= b/k*k) cout << "OK" <<endl;
  else cout << "NG" << endl;
  return 0;
}

// B
#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;
int main(){
  ll x;
  cin >> x;
  ll ans = 0, a = 100;
  while(a <x){
    a += a/100;
    ++ans;
  }
  cout << ans <<endl;
  return 0;
}

// C ※Pythonならitertoolsが使えるらしい
// 深さ優先探索（DFS）：全探索。基本。
#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int n, m, q;
vector<int> a, b, c, d;
int ans;

void dfs(vector<int> A){
  if (A.size() == n+1){ // 終了時の処理
    int now = 0;
    // スコア計算
    rep(i,q){
      if(A[b[i]] - A[a[i]] == c[i]) now += d[i];
    }
    ans = max(ans, now)
    return;
  }

  // 探索処理
  A.push_back(A.back()); // Aの最後の要素をAに追加する
  while(A.back() <= m){ // 末尾がm以下
    dfs(A);
    A.back()++;
  }
}

int main(){
  cin >> n, m, q;
  a = b = c = d = vector<int>(q);
  req(i,q){
    cin >> a[i], b[i], c[i], d[i];
  }
  dfs(vector<int>(1,1));
  cout << ans << endl;
  return 0;
}

// D
