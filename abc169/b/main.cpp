#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); ++i)
#define repf(i,n) for(int i=1; i<(n+1); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main(){

  ll LIM = pow(10,18);

  int N;
  cin >> N;
  vector<ll> A(N);

  ll a;
  ll k;
  rep(i,N){
    cin>>a;
    A.at(i) = a
    k += log10(a)+1
    i
  }

  auto itr = find(A.begin(), A.end(), 0);
  size_t index = distance( A.begin(), itr );

  if (index != A.size()) { // 発見できたとき
    cout<<0;
    return 1;
  }

  ll ans=1;
  rep(i,N){
    ans*=A[i];
    if(ans>LIM){
      cout<<-1;
      return 0;
    }
  }

  cout<<ans;
  return 0;
}
