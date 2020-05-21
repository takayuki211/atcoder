#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); ++i)
#define repf(i,n) for(int i=1; i<(n+1); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main(){

  int N;
  cin >> N;

  ll ans=0;
  repf(i,N){
    if(i%3!=0 && i%5!=0) ans+=i;
  }

  cout<<ans;

  return 0;
}
