#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); ++i)
#define repf(i,n) for(int i=1; i<(n+1); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main(){
  string s;
  cin >> s;
  if (s[2]==s[3] && s[4]==s[5]) cout << "Yes";
  else cout << "No";

  return 0;
}
